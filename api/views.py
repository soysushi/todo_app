from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

#third party
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins

from .models import Todo
from .serializers import TodoSerializer

# permission_classes = (IsAuthenticated, )

# detect when a user is created, and then create a token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Add and Filter TODO
class TodoListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = TodoSerializer
    def get_queryset(self):
        queryset = Todo.objects.all()
        id = self.request.query_params.get('task_id')
        title = self.request.query_params.get('task_title')
        description = self.request.query_params.get('task_description')
        state = self.request.query_params.get('task_state')
        date = self.request.query_params.get('task_due_date')
        user = self.request.query_params.get('user_id')
        if title:
            queryset = queryset.filter(task_title=title)
        elif id:
            queryset = queryset.filter(task_id=id)
        elif description:
            queryset = queryset.filter(task_description=description)
        elif state:
            queryset = queryset.filter(task_state=state)
        elif date:
            queryset = queryset.filter(task_due_date=date)
        elif user:
            queryset = queryset.filter(user_id=user)
        return queryset

# Delete
class TodoDeleteView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        return Todo.objects.all()
