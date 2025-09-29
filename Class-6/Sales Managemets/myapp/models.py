from django.db import models

class ProductModel(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ({self.category}) - {self.unit_price} Tk"

