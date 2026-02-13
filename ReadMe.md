# Office Extension System - Backend Instructions (Django)

## Project Overview
Build a Django REST API backend for an Office Extension System that manages employee contact information. **Employees are registered ONLY from the React frontend, NOT from Django admin.**

## Folder Structure

```
│   │  
│   └── extensions_backend
│   │   └── settings.py                   # Contains all application configurations
│   │   └── urls.py                       # Contains path to all urls in this application
│   │   └── init.py                       # Contains app initialization
│   │  
│   └── extensions_django
│   │   └── serializer
│   │   └── models.py                     # Contains database models(tables) for the project
│   │   └── urls.py                       # Contains endpoint urls for the project
│   │   └── views.py                      # Contains api methods for the project
│   │   └── docker-compose.yml            # Contains docker images and container configurations
│   │   
│   └── .env                              # Contains global configurations
│   └── Dockerfile                        # Contains commands to build docker image for the project
│   └── requirements.txt                  # Contains package dependencies for the project
│   └── manage.py                         # File that controls running state of the app.

```

## Technology Stack

Language: Python3.12

Framework: Django4.2

Database: PostgreSQL

Deployment: Docker (also pulling postgreSQL)



#### Deployment on docker

To deploy the application run the following command in the folder containing the docker compose file:

```
git pull && cd extensions_django && docker-compose down && docker-compose up --build -d && docker-compose logs -f
```

#### Apply migrations on dockerized app.

Open dockerized extensions_backend django interactive terminal with the following command:

```
sudo docker exec -it extensions_backend-django bash
```
Apply migrations using the following command: 

```
python3 manage.py makemigrations && python3 manage.py migrate
```

Exit interactive terminal
