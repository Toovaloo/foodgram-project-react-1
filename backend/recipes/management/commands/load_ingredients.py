import argparse
from csv import reader

from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Measure


class Command(BaseCommand):
    """Ingredients loader."""
    help = "Load ingredients from csv file."

    def add_arguments(self, parser):
        parser.add_argument(
            '--file', type=argparse.FileType('r'), help='Path to the csv file.'
        )

    def handle(self, *args, **kwargs):
        file_obj = kwargs['file']

        csv_reader = reader(file_obj)
        for row in csv_reader:
            if len(row) == 2:
                measure, _ = Measure.objects.get_or_create(name=row[1])
                Ingredient.objects.get_or_create(
                    name=row[0], measurement_unit=measure
                )

        file_obj.close()
