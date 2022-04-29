# Special Thanks
# https://www.youtube.com/watch?v=1FBckemKu1Q

from .importer import Importer
import xmltodict


class XmlImporter(Importer):

    def import_data(fileName):
        Importer.check_extension(fileName, 'xml')
        with open(fileName, 'r') as file:
            xml_data = file.read()
            dict_data = xmltodict.parse(xml_data)
            res = dict(dict_data)['dataset']['record']
            return res
