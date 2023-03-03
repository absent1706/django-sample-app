# django-playground

DRF app that follows this course https://www.youtube.com/playlist?list=PLyaCd9XYVI9DiMvYl-8OdZk7ktc6NQWrb

## Getting started

### Setup Env Vars

create `.env` file and add variables like in `.env.example`

### To run locally

Install `python:3.10`, `pip3`, `pipenv`

Using [pipenv](https://github.com/pypa/pipenv) run `pipenv shell` and `pipenv install` to create virtual environment and install dependencies

```sh
$ pipenv shell
$ pipenv install
```

Go to `src` directory and run

```sh
$ python manage.py migrate
$ python manage.py test
$ python manage.py runserver
```

### To run via docker

Install `Docker` and `docker-compose`

Run 
```sh
$ docker-compose build
$ docker-compose up

```

Open `http://localhost:8000` to view it in the browser

## [Django admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/) web interface (user should be `is_staff` or `is_superuser`)
`http://localhost:8000/admin`


## [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/)
`http://localhost:8000/api/v1/`


## Swagger and Redoc
`http://localhost:8000/api/docs/schema/swagger-ui/`
`http://localhost:8000/api/docs/schema/redoc/`

## YAML schema
`http://localhost:8000/api/docs/schema/`

Use your user credentials to login into the swagger