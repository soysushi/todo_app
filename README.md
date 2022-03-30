
# TODO API
A lightweight TODO list server application. User can create add, delete, and update a TODO object.

## Installation

Getting it up and running with Git

# How to Setup
1. Clone Project
```
git clone https://github.com/soysushi/tribe_inventory.git
```

2. Go To Project Directory
```
cd inventory-management
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



#### Create a TODO

```http
  POST /
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_title`      | `string` | **Required**. task title |
| `task_description`      | `string` | **Required**. description of task |
| `task_state`      | `string` | **Required**. to_do, in_progress, done |
| `task_due_date`      | `date` | **Required**. date field  |

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

This creates the server app, database, and nginx in 3 containers total.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`AUTH_USER_MODEL`

`REST_FRAMEWORK`


## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Usage/Examples

```cURL
curl --location --request POST 'http://127.0.0.1:8000/api/token/' \
--form 'username="test"' \
--form 'password="testpass123"'
```

I recommend using postman to easily test the API endpoints.