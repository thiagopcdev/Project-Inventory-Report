from abc import ABC
from datetime import datetime
from statistics import mode


class SimpleReport(ABC):

    @classmethod
    def get_old_fabrication_date(cls, dictList):
        array_fabrication_date = [
            cls.__formatar(product['data_de_fabricacao'])
            for product in dictList
            ]
        return min(array_fabrication_date).date()

    @classmethod
    def get_nearest_expiration_date(cls, dictList):
        datenow = datetime.now()
        array_expiration_date = [
            cls.__formatar(product['data_de_validade'])
            for product in dictList
            if cls.__formatar(product['data_de_validade']) > datenow
        ]
        return min(array_expiration_date).date()

    @classmethod
    def get_bigger_stock_company(cls, dictList):
        array_companies = [
            product['nome_da_empresa'] for product in dictList
        ]
        return mode(array_companies)

    def __formatar(newDate):
        data = datetime.fromisoformat(newDate)
        return data

    @classmethod
    def generate(cls, dictList):
        return (
            'Data de fabricação mais antiga: '
            f'{cls.get_old_fabrication_date(dictList)}\n'
            'Data de validade mais próxima: '
            f'{cls.get_nearest_expiration_date(dictList)}\n'
            'Empresa com maior quantidade de produtos estocados: '
            f'{cls.get_bigger_stock_company(dictList)}\n'
        )
