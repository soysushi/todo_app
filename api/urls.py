from django.urls import path, include
from .views import TodoListCreateView, TodoDeleteView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('', TodoListCreateView.as_view(), name='create or filter todo'),
    path('delete/<uuid:pk>', TodoDeleteView.as_view(), name='delete todo')
]
