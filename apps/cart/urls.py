from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_cart, name='cart'),
    path('go', views.cart_detail, name='cart-go'),
    path('remove', views.cart_remove, name='cart-remove'),
    path('success/', views.success, name='success')
]