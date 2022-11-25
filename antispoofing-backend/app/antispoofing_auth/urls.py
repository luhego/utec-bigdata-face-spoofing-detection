from django.urls import path

from .views import AuthView

urlpatterns = [
    path("auth/signup", AuthView.as_view(), name="auth_signup"),
]
