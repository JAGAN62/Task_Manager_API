# Task_Manager_API

A RESTful Task Manager API developed using **Django**, **Django REST Framework**, and **JWT Authentication**.

## Project Overview
This project allows users to register, log in securely using JWT, and manage their personal tasks. Each authenticated user can create, view, update, and delete only their own tasks.

# Features
- User Registration
- User Login
- JWT Authentication
- Create Task
- View All Tasks
- View Single Task
- Update Task
- Delete Task
- SQLite Database
- Input Validation
- Error Handling
- Django Admin Panel

## Technologies Used
- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Git & GitHub

# Activate the virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Data base schema
User ->
id
username
email
password

Task ->
id
title
description
status
owner (ForeignKey -> User)
created_at
updated_at

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver

# Server URL:
http://127.0.0.1:8000/

# Authentication
This project uses **JWT Authentication**.
Include the access token in the request header:

Authorization: Bearer <your_access_token>

## API Endpoints User
`/api/register/` | Register a new user 
`/api/login/` | Login and receive JWT token

# Tasks
`/api/tasks/` | Retrieve all tasks |
`/api/tasks/create/` | Create a new task |
`/api/tasks/detail/<id>/` | Retrieve a specific task |
`/api/tasks/update/<id>/` | Update a task |
`/api/tasks/delete/<id>/` | Delete a task |

## Sample Register Request
{
    "username": "jagan",
    "email": "jagan@example.com",
    "password": "password123"
}

## Sample Create Task Request
{
    "title": "Complete Django Assignment",
    "description": "Finish the technical assessment",
    "status": "Pending"
}

## Database
The project uses **SQLite** as the database for development.

## Assumptions and Design Decisions
- The project uses SQLite for simplicity and easy setup.
- JWT Authentication is used to secure protected endpoints.
- Each user can access and manage only their own tasks.
- Django REST Framework serializers are used for input validation.
- Proper HTTP status codes are returned for success and error responses.

#Author
**Mamanduru Jagan**
GitHub: https://github.com/JAGAN62