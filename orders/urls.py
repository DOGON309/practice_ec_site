from django.urls import path
from .views import OrderHistoryView, OrderDetailView

urlpatterns = [
    path('', OrderHistoryView.as_view()),
    path('<str:id>', OrderDetailView.as_view()),
]
