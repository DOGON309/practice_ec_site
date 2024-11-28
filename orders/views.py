from django.views.generic import ListView, DetailView
from .models import Order, OrderItem

class OrderHistoryView(ListView):
    model = Order
    ordering = '-order_date'

class OrderDetailView(DetailView):
    model = Order
    