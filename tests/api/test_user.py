# find a way to get the created user from users model
# send the model to get the api key

# attach api key to request, login the user
# while logged in
    # perform API requests

import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from api.models import Todo
import os
client = APIClient()

# The token is created when username and password passed into the Token object
# Token that is returned is unique to that user and is included in the header under "Authorization" 
# The view itself requires that the user is Authenticated with the unique api key
def test_new_user(django_user_model):
    test_user = django_user_model.objects.create(username="someone", password="something")
    client.force_login(test_user)
    token = Token.objects.create(user=test_user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.get('http://localhost:1337/')
    data = response
    assert response.status_code == 200
    # add a todo
    new_todo = dict(
        task_id="e092bd74-909c-4aa4-b498-059a95d83104",
        task_title="title",
        task_description="description",
        user_id=test_user.uuid,
    )
    response = client.post('/', new_todo)
    data = response
    assert response.status_code == 201
    # update a todo
    new_todo = dict(
        task_id="e092bd74-909c-4aa4-b498-059a95d83104",
        task_title="title changed",
        task_description="description",
        user_id=test_user.uuid,
    )
    response = client.put('/delete/e092bd74-909c-4aa4-b498-059a95d83104', new_todo)
    assert response.status_code == 200
    # delete a todo
    response = client.delete('/delete/e092bd74-909c-4aa4-b498-059a95d83104',)
    data = response
    assert response.status_code == 204

# test to get key in environment.
def test_get_env_variables():
    u = os.environ['USER']
    p = os.environ['PASSWORD']
    t = os.environ['TOKEN']
    assert u == 'test_user'
    assert p == 'testpass123'
    assert t == '0969eb28a6369296f42dc36f271336d6e69d1297'

