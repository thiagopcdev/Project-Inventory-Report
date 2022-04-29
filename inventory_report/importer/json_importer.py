from .importer import Importer
import json


class JsonImporter(Importer):

    def import_data(fileName):
        Importer.check_extension(fileName, 'json')
        with open(fileName, 'r') as file:
            return json.load(file)
