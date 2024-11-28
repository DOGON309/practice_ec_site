from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic

from .models import Product

# Create your views here.
class ProductsListView(TemplateView):
    template_name = 'products/product_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product_items = Product.objects.all()
        ctx['products'] = product_items
        return ctx

class ProductsDetailView(TemplateView):
    template_name = 'products/product_detail.html'
    mdoel = Product

    def get_context_data(self, id, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product_item = Product.objects.get(id = id)
        ctx['product'] = product_item
        return ctx
