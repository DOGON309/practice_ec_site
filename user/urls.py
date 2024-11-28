from django.urls import path
from .views import IndexView, SignUpView, LoginView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

