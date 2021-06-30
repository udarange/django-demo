# Django

Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern.

To start cli

```
pipenv shell
```

### To start a new project,

```.env
django-admin startproject djangodemo .
```

### To run,

```
django-admin runserver
```
or
```.env
python3 manage.py runserver
```
maybe need this, `pip install django --upgrade`


#### INSTALLED_APPS

```.env
INSTALLED_APPS = [
    'django.contrib.admin', // admin interface
    'django.contrib.auth', // authenticating users
    'django.contrib.contenttypes',
    'django.contrib.sessions', // tempory memeory on server
    'django.contrib.messages', // one time notification
    'django.contrib.staticfiles', 
]
```

### create a new app
```.env
python3 manage.py startapp playground
```

view more on [django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
