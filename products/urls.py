from django.urls import path
from .views import ProductsListView, ProductsDetailView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_info_view'),
    path('<uuid:id>/', ProductsDetailView.as_view(), name='products_list_view'),
]
