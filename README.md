
# TODO API
A lightweight TODO list server application. User can create add, delete, and update a TODO object. Comes with django admin in default /admin url.

## Installation

Getting it up and running with Git

# How to Setup
1. Clone Project
```
git clone https://github.com/soysushi/todo_app.git
```

2. Go To Project Directory
```
cd todo_app
```
3. Create Virtual Environment
```
python3 -m venv venv
```
4. Active Virtual Environment
```
source venv/bin/activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Migrate Database
```
python manage.py migrate
```
7. Create Super User
```
python manage.py createsuperuser
```
8. Run Project
```
python manage.py runserver
```

    

## API Reference

#### Attain auth token for user

```http
  POST /api/token
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

#### Get TODOS, default is list all. You can also filter by specific field(s)

```http
  GET /
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_id`      | `uuid` | **Optional**. Id of todo to fetch |
| `task_title`      | `string` | **Optional**. task title |
| `task_description`      | `string` | **Optional**. description of task |
| `task_state`      | `string` | **Strict**. to_do, in_progress, done |
| `task_due_date`      | `date` | **Optional**. date field  |
| `user_id`      | `uuid` | **Optional**. A specific user's todos |



#### ADD a TODO

```http
  POST /
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_title`      | `string` | **Required**. task title |
| `task_description`      | `string` | **Required**. description of task |
| `task_state`      | `string` | **Required**. to_do, in_progress, done |
| `task_due_date`      | `date` | **Required**. date field  |


#### DELETE a TODO

```http
  DELETE /delete/<uuid:task_id>
```
Will return http status code 204 when deleted


#### UPDATE a TODO

```http
  PUT /delete
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_title`      | `string` | **Required**. task title |
| `task_description`      | `string` | **Required**. description of task |
| `user_id`      | `uuid` | **Required**. user's uuid - can be seen in django admin |

## Docker 

To run a docker image of this project, make sure you have docker installed.

1. Build the docker image
```
docker build .
```

2. Compose in detached mode
```
docker-compose up -d --build
```
3. Create Super User
```
docker-compose exec web python manage.py createsuperuser
```

4. Shut everything down
```
docker-compose down
```
This creates the server app, database, and nginx in 3 containers total.


## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Usage/Examples

## Get API Key from command line 
```cURL
curl --location --request POST 'http://127.0.0.1:8000/api/token/' \
--form 'username="test"' \
--form 'password="testpass123"'
```

## Update a TODO
```
curl --location --request PUT 'http://localhost:8000/delete/35cdd318-1081-4a22-8e8a-14c3ec744798' \
--header 'Authorization: token 0969eb28a6369296f42dc36f271336d6e69d1297' \
--form 'task_title="test"' \
--form 'task_description="testpass123"' \
--form 'user_id="6d57a688-5e51-4926-943c-7fd06b5cf55f"'
```

## Delete a TODO
curl --location --request DELETE 'http://localhost:8000/delete/f4e55ff0-6ee0-49a5-8fde-e1849371145f' \
--header 'Authorization: token 0969eb28a6369296f42dc36f271336d6e69d1297'

I recommend using postman to easily test the API endpoints. 

Every API endpoint has a mixin, so it needs the token attained from either /api/token, cURL, or logging into django admin