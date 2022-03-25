from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from rest_framework_api_key.admin import APIKeyModelAdmin
from .models import CustomUserAPIKey

CustomUser = get_user_model()

@admin.register(CustomUserAPIKey)
class CustomUserAPIKeyModelAdmin(APIKeyModelAdmin):
    pass

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'api_keys']

admin.site.register(CustomUser, CustomUserAdmin)
