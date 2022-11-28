from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    genre = models.CharField(max_length=255, blank=True, null=True)
    video_s3_url = models.CharField(max_length=100, blank=True, null=True)


class LoginAttempt(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    video_s3_url = models.CharField(max_length=100, blank=True, null=True)
