from .importer import Importer
import csv


class CsvImporter(Importer):

    def import_data(fileName):
        Importer.check_extension(fileName, 'csv')
        with open(fileName, 'r') as file:
            return list(csv.DictReader(file))
