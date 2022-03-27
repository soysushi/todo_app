from django.urls import path, include
from .views import TestView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test')
]
