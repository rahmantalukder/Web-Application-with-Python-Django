from django.shortcuts import render, redirect
from myapp.models import *
# Create your views here.
def basePages(request):
    
    return render(request, 'base.html')


def ProductPages(request):
    if request.method=="POST":
        product_name = request.POST.get("product_name")
        category = request.POST.get("category")
        unit_price = float(request.POST.get("unit_price"))
        quantity = int(request.POST.get("quantity"))
        discount_percent = float(request.POST.get("discount_percent"))
        tax_percent = float(request.POST.get("tax_percent"))
        
        if unit_price:
            total_price=(unit_price*quantity)-((unit_price*quantity)*discount_percent/100)+ ((unit_price*quantity))*tax_percent/100

        data=ProductModel(
            product_name=product_name,
            category=category,
            unit_price=unit_price,
            quantity=quantity,
            discount_percent=discount_percent,
            tax_percent=tax_percent,
            total_price=total_price,
        ).save()
        return redirect("ProductListPages")

    return render(request, 'product_form.html')

def ProductListPages(request):
    context={
        'product':ProductModel.objects.all()
    }

    return render (request, 'Product_List__Pages.html',context)

def LoginPages(request):

    return render(request, 'login.html')

