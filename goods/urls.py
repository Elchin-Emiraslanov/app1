from django.urls import path
from goods.views import *

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/',
        catalog,
        name='index'
        ),
        
    path('<slug:category_slug>/<int:page>/',
        catalog,
        name='index'
        ),
 
    path('product/<slug:product_slug>/',
        product,
         name='product',
        ),


    
    
]