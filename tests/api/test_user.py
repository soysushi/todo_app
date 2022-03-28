# find a way to get the created user from users model
# send the model to get the api key

# attach api key to request, login the user
# while logged in
    # perform API requests

import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
client = APIClient()

def test_new_user(django_user_model):
    test_user = django_user_model.objects.create(username="someone", password="something")
    client.force_login(test_user)
    token = Token.objects.create(user=test_user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.get('/')
    data = response
    assert response.status_code == 200