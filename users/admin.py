from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from rest_framework_api_key.admin import APIKeyModelAdmin

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['uuid', 'email', 'api_key']

admin.site.register(CustomUser, CustomUserAdmin)
