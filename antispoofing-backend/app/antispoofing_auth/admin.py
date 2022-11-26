from django.contrib import admin

from .models import CustomUser, LoginAttempt


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "genre", "video_hex_code")


class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "success", "timestamp", "video_hex_code")


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(LoginAttempt, LoginAttemptAdmin)
