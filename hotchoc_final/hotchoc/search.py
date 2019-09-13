from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, DocType, Keyword, Date

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

from elasticsearch_dsl import Document, Text, Date, Search

def search(suggester):
    s = Search().filter('term', suggester=suggester)
    response = s.execute()
    return response  # return a list of hot chocolate stores

def bulk_indexing():
    HotChocStoreIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(hc.indexing() for hc in models.HotChocStore.objects.all().iterator()))

connections.create_connection(hosts=["127.0.0.1"])

class HotChocStoreIndex(Document):
    location = Text(fields={'keyword': Keyword()})
    suggester = Text(fields={'keyword': Keyword()})
    created_at = Date()
    name = Text()
    description = Text()

    class Index:
        name = 'hotchocstore-index'
