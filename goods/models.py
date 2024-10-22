from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='url')

    class Meta:
        db_table = 'category'
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return f"{self.name}"

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Url')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Image')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Discount in %')
    quantity = models.PositiveIntegerField(default=0, verbose_name="Stock")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="category")

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ("id",)

    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    
    def display_id(self):
        return f"{self.id:05}"
        
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price