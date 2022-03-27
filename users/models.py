# Create your models here.
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db import models
import uuid


class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    email = models.EmailField(unique=True)
