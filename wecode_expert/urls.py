from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('users', include('users.urls')),
    path('products', include('products.urls')),
    path('orders', include('orders.urls'))
]
