from abc import ABC, abstractmethod


class Importer(ABC):

    def check_extension(fileName, ext):
        if ext not in fileName:
            raise ValueError('Arquivo inválido')

    @abstractmethod
    def import_data(fileName): pass
