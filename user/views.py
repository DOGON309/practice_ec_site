from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm
from products.models import Product

class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product_items = Product.objects.all()
        ctx["products"] = product_items
        return ctx

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('user:index')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return redirect('register')

class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

class LogoutView(LoginRequiredMixin, BaseLogoutView):
    succeess_url = reverse_lazy('user:login')