# django-playground

DRF app that follows this course https://www.youtube.com/playlist?list=PLyaCd9XYVI9DiMvYl-8OdZk7ktc6NQWrb

## Getting started

### Setup Env Vars

create `.env` file and add variables like in `.env.example`

### To run locally

Install `python:3.10`, `pip3`, `virtualenv`

```sh
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run DB 

```
docker-compose up -d postgres
docker-compose logs -f
```

Run app

```sh
cd src
python manage.py migrate
python manage.py runserver
```

### To run via docker

Install `Docker` and `docker-compose`

Run 
```sh
docker-compose up --build
```

Open `http://localhost:8000` to view it in the browser

#### Optional: enable live reload when running via Docker
Before running docker-compose, do

`cp docker-compose.override.local.yml docker-compose.override.yml`

### To run via HTTPS on custom domain

> This config is not yet production-ready!

1 . You must have own a domain and setup DNS server to have an A record pointing to an IP of VM you are on.

2 . In .env file, uncomment and adjust env vars under `HTTPS + custom domain` section

3 . Run
```
docker-compose -f docker-compose.yaml -f docker-compose.https.yml up -d --build
```

## Run tests

```
python manage.py test
```

To enable coverage, type
```
coverage run --source='.' manage.py test 
coverage report
```

You may also type `coverage html` to get detailed HTML report in `htmlcov` folder


## [Django admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/) web interface (user should be `is_staff` or `is_superuser`)

Create superuser
```
python manage.py createsuperuser
```

Then visit `http://localhost:8000/admin`
