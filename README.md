# Welcome to Introduction to Elasticsearch with Django!

This is a pretty simple workshop to get your feet wet and provide you some extra info on Elasticsearch and what you may want to do with it, as well as a very simple integration to get started and carry away with you.

We're building a hot chocolate store locator!

## Connect to Elasticsearch

Download Elasticsearch 6.5.4 and run it locally, then connect to localhost:9200.

Either way, you should see a JSON response full of version numbers.

    # Linux and Mac OS
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.5.4.tar.gz

    # other platforms https://www.elastic.co/downloads/past-releases/elasticsearch-6-5-4

## Fill it with data.

### Get the app started

So we have model objects to index!

    1. create a virtual environment and activate it
    2. pip install -r hotchoc_final/requirements.txt
    3. django-admin startproject hotchocproj
    4. cd hotchocproj
    5. python manage.py startapp hotchoc
    6. add 'hotchoc' to INSTALLED_APPS in settings.py (see hotchoc_final/hotchoc/settings.py if in doubt)
    7. Next, copy over hotchoc_final/hotchoc/models.py to your hotchocproj/hotchoc/models.py. We'll take a look at the code together.
    8. Put this in admin.py (same level as models.py)

    from django.contrib import admin
    from .models import HotChocStore

    admin.site.register(HotChocStore)

### Bulk index

    1. Copy over search.py from the hotchoc_final directory to your hotchocproj/hotchoc/. We'll stop and have a look at the file.
    2. python manage.py makemigrations
    3. python manage.py migrate
    4. python manage.py createsuperuser
    5. Note how models.py has an indexing method too to complement the bulk indexing
    6. Data model in place, mapping to index in place, we can finally get data in!
    7. copy over the hotchoc_final/hotchoc/management directory into your hotchocproj/hotchoc/ app.
    8. copy hotchoc_final/hotchoc/agg_setup.py to your hotchocproj/hotchoc/ app.

    python manage.py gendata

## Search

    4. Let's play. Run

    python manage.py shell

    # and then type into the Python shell

    from hotchoc.search import search
    hits = search(suggester='emanuil')
    len(hits) # you should get 4

    hits = search(suggester='Emanuil')
    len(hits) # why are there 0 hits? It's 'Emanuil' in the data! We'll come back to this.

    # Look at the code in hotchoc.search too.

    5. Alright, we've done some searching. But sometimes you want the data to tell you what to search for. E.g. see https://www.world-nuclear.org/information-library/facts-and-figures/reactor-database-search.aspx .

    from hotchoc import agg_setup
    agg_s = agg_setup.HotChocStoreSearch()
    agg_s.aggs.bucket('by_suggester', 'terms', field='suggester.keyword')
    r = agg_s.execute()
    r.aggs.by_suggester.to_dict()

    6. Hang on, why did that say .keyword? And why did my name only work when searched lowercase? The answer is "analysis", index-time and query analysis.

    Let's try without .keyword.

    # quit Python now to prevent elasticsearch_dsl caching, then restart it

    from hotchoc import agg_setup
    agg_s = agg_setup.HotChocStoreSearch()
    agg_s.aggs.bucket('by_suggester', 'terms', field='suggester')
    r = agg_s.execute()  # boom. What happened?

    7. We've done indexing, searching with a filter and an aggregation. Let's do a full-text search.

    from elasticsearch_dsl import Search
    s = Search().query('query_string', query='the best')  # should get 1 result
