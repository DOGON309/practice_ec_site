from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from products.models import Product
from .models import Cart

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        cart_items = Cart.objects.filter(user = self.request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        ctx['cart_items'] = cart_items
        ctx['total_price'] = total_price
        return ctx

class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        quantity = int(request.GET.get("quantity", 1))

        cart_item, created = Cart.objects.get_or_create(user = request.user, product = product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return redirect("cart")

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get("quantity", 1))

        cart_item, created = Cart.objects.get_or_create(user = request.user, product = product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return redirect("cart")

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item = Cart.objects.filter(user = request.user, product = product)
        if cart_item:
            cart_item.delete()
        return redirect("cart")
    