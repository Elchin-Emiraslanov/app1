from django.urls import path



app_name = 'goods'

urlpatterns = [
    path('',
        catalog,
        name='index'
        ),

    path('product/',
        product,
         name='product',
           )
]