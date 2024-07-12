from tabnanny import verbose
from django.db import models 
from goods.models import Products

from users.models import User


class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.produsts_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    
class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="User", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date create order")
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")
    requires_delievery = models.BooleanField(default=False, verbose_name="delivery required")
    delivery_address = models.TextField(null=True, blank=True, verbose_name='delivery adress')
    payment_on_get = models.BooleanField(default=False, verbose_name="Payment upon receipt")
    is_paid = models.BooleanField(default=False, verbose_name="Done")
    status = models.CharField(max_length=50, default='In processing', verbose_name="status order")

    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

        def __str__(self) -> str:
            return f"Order N {self.pk} | Buyer {self.user.first_name}  {self.user.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Order")
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Product", default=None)
    name = models.CharField(max_length=150, verbose_name="Name")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Sell date')

    class Meta:
        db_table = 'order_item'
        verbose_name = "Sold product"
        verbose_name_plural = "Sold products"

    def products_price(self):
        return round(self.price * self.quantity, 2)
    
    def __str__(self) -> str:
        return f"Product {self.name} | Order N {self.order.pk}"
    

