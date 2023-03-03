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
python manage.py test
python manage.py runserver
```

### To run via docker

Install `Docker` and `docker-compose`

Run 
```sh
docker-compose up --build
```

Open `http://localhost:8000` to view it in the browser

## [Django admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/) web interface (user should be `is_staff` or `is_superuser`)

Create superuser
```
python manage.py createsuperuser
```

Then visit `http://localhost:8000/admin`
