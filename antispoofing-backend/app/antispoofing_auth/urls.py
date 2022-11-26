from django.urls import path

from .views import SignupView, LoginView

urlpatterns = [
    path("auth/signup", SignupView.as_view(), name="auth_signup"),
    path("auth/login", LoginView.as_view(), name="auth_login"),
]
