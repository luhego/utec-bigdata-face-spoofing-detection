from django.contrib import admin

from .models import CustomUser, LoginAttempt


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "genre", "video_s3_url")


class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "success", "timestamp", "video_s3_url")


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(LoginAttempt, LoginAttemptAdmin)
