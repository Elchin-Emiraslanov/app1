from django.contrib import admin
from goods.models import*

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class Categories(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class Products(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}