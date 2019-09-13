from django.core.management.base import BaseCommand
from django.core.management import call_command
from hotchoc import models
from hotchoc.search import bulk_indexing, HotChocStoreIndex
from elasticsearch_dsl import Index

class Command(BaseCommand):
    help = 'Generates sample data for the workshop'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Emptying the DB'))
        models.HotChocStore.objects.all().delete()

        models.HotChocStore(location='London', suggester='Emanuil', name='Store 1', description='the best').save()
        models.HotChocStore(location='London', suggester='Jane', name='Store 2').save()
        models.HotChocStore(location='Cardiff', suggester='Joe', name='Store 3').save()
        models.HotChocStore(location='Cardiff', suggester='Emanuil', name='Store 4').save()
        models.HotChocStore(location='Edinburgh', suggester='Emanuil', name='Store 5').save()
        models.HotChocStore(location='Heidelberg', suggester='David', name='Store 6', description='very central').save()
        models.HotChocStore(location='London', suggester='Rebecca', name='Store 7').save()
        models.HotChocStore(location='London', suggester='Ryan', name='Store 8').save()
        models.HotChocStore(location='London', suggester='Latisha', name='Store 9').save()
        models.HotChocStore(location='London', suggester='Emanuil', name='Store 10', description='so so').save()

        self.stdout.write(self.style.SUCCESS('Successfully saved 10 stores.'))

        self.stdout.write(self.style.SUCCESS('Emptying the index'))
        Index(HotChocStoreIndex.Index.name).delete(ignore=[400, 404])

        bulk_indexing()

        self.stdout.write(self.style.SUCCESS('Successfully indexed 10 stores into ES.'))
