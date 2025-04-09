### set up virtual environment to install django
```bash
python -m venv env
source env/bin/activate
pip install django
```

### Create a Django Project
```bash
django-admin startproject django_demo
cd django_demo
```

### Create an App
```bash
python manage.py startapp blog
```

Add your app to INSTALLED_APPS in mysite/settings.py.

