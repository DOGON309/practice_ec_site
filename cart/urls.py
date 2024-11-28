from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<uuid:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<uuid:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
