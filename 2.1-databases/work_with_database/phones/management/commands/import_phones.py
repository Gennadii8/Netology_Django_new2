import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

# Get data from .csv by lines, import them to database with terminal command: python manage.py import_phones


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            tel = Phone.objects.create(
                id=phone['id'],
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
            )
            tel.slug

