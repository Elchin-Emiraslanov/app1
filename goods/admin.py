from django.contrib import admin
from goods.models import*

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class Categories(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class Products(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount', ]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]