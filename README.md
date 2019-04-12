# Welcome to Introduction to Elasticsearch with Django!

This is a pretty simple workshop to get your feet wet and provide you some extra info on Elasticsearch and what you may want to do with it, as well as a very simple integration to get started and carry away with you.

We're building a hot chocolate store locator.

## Connect to Elasticsearch

10.5.250.245:9200 in your browsers. (IP may change)
Alternatively, download Elasticsearch 6.5.4 and run it locally, then connect to localhost:9200.

Either way, you should see a JSON response full of version numbers.

    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.5.4.tar.gz
    # multi-platform https://www.elastic.co/downloads/past-releases/elasticsearch-6-5-4

## Fill it with data.

But first

### Get the app started

So we have model objects to index!

    1. create a virtual environment and activate it
    2. pip install django elasticsearch-dsl
    3. django-admin startproject myapp
    4. cd myapp
    5. python manage.py startapp myapp
    6. add 'myapp' to INSTALLED_APPS in settings.py (see hotchoc_final/settings.py if in doubt)
    7. Next, copy over hotchoc_final/models.py to your models.py. We'll take a look at the code together.
    8. Put this in admin.py (same level as models.py)

    from django.contrib import admin
    from .models import BlogPost

    admin.site.register(HotChocStore)

    9. python manage.py makemigrations
    10. python manage.py migrate
    11. python manage.py createsuperuser
    12. python manage.py runserver
    13. go to http://localhost:8000/admin/ and login

### Bulk index

    1. Copy over search.py from the hotchoc_final directory. We'll stop and have a look at the file.
    2. Note how models.py has an indexing method too to complement the bulk indexing

## Search

### Faceted Search
