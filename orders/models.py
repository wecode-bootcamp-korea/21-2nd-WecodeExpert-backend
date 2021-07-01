from django.db import models

class Order(models.Model):
    created_at   = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    price        = models.DecimalField(max_digits=8, decimal_places=2)
    user         = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    product      = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'