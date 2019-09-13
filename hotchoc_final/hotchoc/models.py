from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import HotChocStoreIndex

# Create your models here

class Suggester(models.Model):
    name = models.CharField(max_length=200)

# Hot chocolate to be indexed into ElasticSearch
class HotChocStore(models.Model):
    location = models.CharField(max_length=200)
    suggester = models.CharField(max_length=200)
    created_at = models.DateField(default=timezone.now)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    # Add indexing method to the model
    def indexing(self):
       obj = HotChocStoreIndex(
          meta={'id': self.id},
          suggester=self.suggester,
          created_at=self.created_at,
          name=self.name,
          description=self.description,
          location=self.location
       )
       obj.save()
       return obj.to_dict(include_meta=True)
