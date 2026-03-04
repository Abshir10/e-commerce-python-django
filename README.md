pip install django
django-admin startproject mysite .
python manage.py startapp myapp
Open mysite/settings.py and add 'myapp', to the INSTALLED_APPS list.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', # Add your app here
]

python manage.py migrate
python manage.py createsuperuser


python manage.py runserver
