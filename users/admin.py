from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dislay = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

    inlines = [CartTabAdmin, OrderTabulareAdmin]
