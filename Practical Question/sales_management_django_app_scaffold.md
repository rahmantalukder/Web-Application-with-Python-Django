# Sales Management — Django App Scaffold

This document contains a ready-to-use Django app named **`sales`** inside a project named **`sales_project`**. It includes models, forms, views, templates and instructions so you can create, run, and extend a Sales Management application where users can add sales records and view simple sales reports.

---

## Quick Setup (commands)

```bash
# 1. Create virtualenv and activate
python -m venv env
source env/bin/activate   # on Windows: env\Scripts\activate

# 2. Install Django
pip install django

# 3. Create project and app (or use files below)
django-admin startproject sales_project .
python manage.py startapp sales

# 4. Add 'sales' to INSTALLED_APPS in sales_project/settings.py
# 5. Make migrations and run
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # optional for admin
python manage.py runserver
```

---

## Project structure (provided)

```
sales_project/
├── manage.py
├── sales_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── sales/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── sales/
    │       ├── base.html
    │       ├── sale_list.html
    │       ├── sale_form.html
    │       └── report.html
    └── migrations/
```

---

## `sales/models.py`

```python
from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Sale(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product.name} — {self.quantity} @ {self.unit_price} on {self.date}"

    def get_absolute_url(self):
        return reverse('sales:list')
```

Notes:
- `Sale.unit_price` is stored per row so historical prices are preserved even if `Product.unit_price` changes.

---

## `sales/admin.py`

```python
from django.contrib import admin
from .models import Customer, Product, Sale

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'unit_price')
    search_fields = ('name', 'sku')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'quantity', 'unit_price', 'total')
    list_filter = ('date', 'product')
    date_hierarchy = 'date'
```

---

## `sales/forms.py`

```python
from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['date', 'customer', 'product', 'quantity', 'unit_price', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }
```

---

## `sales/views.py`

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F, FloatField
from django.urls import reverse
from .models import Sale, Product
from .forms import SaleForm
from datetime import date

# List all sales
def sale_list(request):
    qs = Sale.objects.select_related('product', 'customer').all()
    return render(request, 'sales/sale_list.html', {'sales': qs})

# Create a new sale
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:list')
    else:
        # Pre-fill unit_price from product when product provided via GET (optional)
        form = SaleForm()
    return render(request, 'sales/sale_form.html', {'form': form})

# Simple reports page
def report(request):
    # filters
    start = request.GET.get('start')
    end = request.GET.get('end')
    sales = Sale.objects.all()
    if start:
        sales = sales.filter(date__gte=start)
    if end:
        sales = sales.filter(date__lte=end)

    # aggregates
    total_revenue = sales.aggregate(total=Sum(F('quantity') * F('unit_price'), output_field=FloatField()))['total'] or 0

    # revenue by product
    by_product = (
        sales.values('product__id', 'product__name')
             .annotate(revenue=Sum(F('quantity') * F('unit_price'), output_field=FloatField()))
             .order_by('-revenue')
    )

    # monthly totals (simple)
    from django.db.models.functions import TruncMonth
    monthly = (
        sales.annotate(month=TruncMonth('date'))
             .values('month')
             .annotate(total=Sum(F('quantity') * F('unit_price'), output_field=FloatField()))
             .order_by('month')
    )

    context = {
        'total_revenue': total_revenue,
        'by_product': by_product,
        'monthly': monthly,
        'start': start,
        'end': end,
    }
    return render(request, 'sales/report.html', context)
```

---

## `sales/urls.py`

```python
from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sale_list, name='list'),
    path('add/', views.sale_create, name='add'),
    path('report/', views.report, name='report'),
]
```

---

## `sales_project/urls.py` (project-level)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls', namespace='sales')),
]
```

---

## `sales/templates/sales/base.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Sales Management</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/modern-css-reset/dist/reset.min.css">
  <style>
    body{font-family: system-ui, Arial; padding: 20px; max-width:1100px; margin:0 auto}
    header{display:flex; gap:12px; align-items:center; margin-bottom:18px}
    nav a{margin-right:12px}
    table{width:100%; border-collapse:collapse}
    th,td{padding:8px; border:1px solid #ddd}
    .muted{color:#666; font-size:.9rem}
  </style>
</head>
<body>
  <header>
    <h1>Sales Management</h1>
    <nav>
      <a href="{% url 'sales:list' %}">Sales</a>
      <a href="{% url 'sales:add' %}">Add Sale</a>
      <a href="{% url 'sales:report' %}">Reports</a>
      <a href="/admin/">Admin</a>
    </nav>
  </header>
  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

---

## `sales/templates/sales/sale_list.html`

```html
{% extends 'sales/base.html' %}
{% block content %}
<h2>Sales</h2>
{% if sales %}
<table>
  <thead>
    <tr><th>Date</th><th>Product</th><th>Customer</th><th>Qty</th><th>Unit</th><th>Total</th><th>Note</th></tr>
  </thead>
  <tbody>
    {% for s in sales %}
    <tr>
      <td>{{ s.date }}</td>
      <td>{{ s.product.name }}</td>
      <td>{{ s.customer.name if s.customer else '' }}</td>
      <td>{{ s.quantity }}</td>
      <td>{{ s.unit_price }}</td>
      <td>{{ s.total }}</td>
      <td class="muted">{{ s.note|default_if_none:'' }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<p>No sales yet. <a href="{% url 'sales:add' %}">Add the first sale</a>.</p>
{% endif %}
{% endblock %}
```

---

## `sales/templates/sales/sale_form.html`

```html
{% extends 'sales/base.html' %}
{% block content %}
  <h2>Add sale</h2>
  <form method="post">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
    </table>
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

---

## `sales/templates/sales/report.html`

```html
{% extends 'sales/base.html' %}
{% block content %}
  <h2>Reports</h2>
  <form method="get" style="margin-bottom:12px">
    <label>Start: <input type="date" name="start" value="{{ start }}"></label>
    <label>End: <input type="date" name="end" value="{{ end }}"></label>
    <button type="submit">Filter</button>
  </form>

  <h3>Total revenue: {{ total_revenue|floatformat:2 }}</h3>

  <h4>Revenue by product</h4>
  <table>
    <thead><tr><th>Product</th><th>Revenue</th></tr></thead>
    <tbody>
      {% for p in by_product %}
      <tr>
        <td>{{ p.product__name }}</td>
        <td>{{ p.revenue|floatformat:2 }}</td>
      </tr>
      {% empty %}
      <tr><td colspan="2">No data</td></tr>
      {% endfor %}
    </tbody>
  </table>

  <h4>Monthly totals</h4>
  <table>
    <thead><tr><th>Month</th><th>Total</th></tr></thead>
    <tbody>
      {% for m in monthly %}
      <tr>
        <td>{{ m.month|date:'Y-m' }}</td>
        <td>{{ m.total|floatformat:2 }}</td>
      </tr>
      {% empty %}
      <tr><td colspan="2">No data</td></tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

---

## `sales_project/settings.py` — important additions

Make sure to add `'sales'` to `INSTALLED_APPS`.

Also (for simplicity) ensure templates DIRs include `BASE_DIR / 'templates'` or app template loading is enabled (default is fine). For static files in development, default is OK.

If you want to allow easier decimal math in Sqlite, no change required. Use `TIME_ZONE` as appropriate for your region.

---

## Extras & Next steps

- Improve UX: add JS to auto-fill `unit_price` when product selected.
- Add validation to `SaleForm` to ensure `unit_price` is positive and not zero.
- Add edit/delete views for sales.
- Add CSV export for reports and/or charts.
- Add authentication: require login to add/view sales.
- Add pagination to `sale_list`.

---

## Example data (optional fixtures)

You can create some products and customers in the admin panel or create a `loaddata` fixture. Example via shell:

```bash
python manage.py shell
```

```python
from sales.models import Product, Customer, Sale
p = Product.objects.create(name='Widget A', sku='W-A', unit_price=120.00)
c = Customer.objects.create(name='ABC Ltd', email='contact@abc.com')
Sale.objects.create(date='2025-09-01', product=p, quantity=3, unit_price=120.00, customer=c)
```

---

If you'd like, I can:
- generate full file contents as individual files ready to download, or
- add authentication and restrict pages to logged-in users, or
- create CSV export and charts on the reports page.

Tell me which extras you want and I'll add them.

