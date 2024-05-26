from django.shortcuts import render
from .models import *
# Create your views here.
def catalog(request):

    goods = Products.objects.all()

    context={
        'title': 'Home - catalog',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')