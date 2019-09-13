from elasticsearch_dsl import Search
from hotchoc import models

class HotChocStoreSearch(Search):
    doc_types = [models.HotChocStore, ]
    # fields that should be searched
    fields = ['suggester', 'name', 'location']
