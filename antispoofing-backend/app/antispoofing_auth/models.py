from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    genre = models.CharField(max_length=255, blank=True, null=True)
    video_hex_code = models.CharField(max_length=64, blank=True, null=True)
    video = models.FileField(max_length=100, blank=True, null=True)


class LoginAttempt(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    video_hex_code = models.CharField(max_length=64, blank=True, null=True)
    video = models.FileField(max_length=100, blank=True, null=True)
