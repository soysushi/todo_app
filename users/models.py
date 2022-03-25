# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_api_key.permissions import HasAPIKey
import uuid


class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    api_key = [HasAPIKey]
