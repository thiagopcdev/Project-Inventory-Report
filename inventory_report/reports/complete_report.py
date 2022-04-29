from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(dictList):
        get_simple_report = SimpleReport.generate(dictList)
        stock_phrase = '\nProdutos estocados por empresa: \n'
        complete_report = get_simple_report + stock_phrase
        business_list = {}

        for item in dictList:
            if item['nome_da_empresa'] not in business_list:
                business_list[item['nome_da_empresa']] = 1
            else:
                business_list[item['nome_da_empresa']] += 1
        for business in business_list.items():
            complete_report += f'- {business[0]}: {business[1]}\n'

        return complete_report
