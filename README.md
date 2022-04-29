## Projeto Relatório de Estoque!

### Habilidades

- Você vai aprender sobre paradigmas de programação
- Conceitos de OO na prática, criando classes e instâncias
- Leitura e escria de arquivos

---

Neste projeto, utilizei a Programação Orientada a Objetos! Implementei um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- Através da importação de um arquivo `XML`;

Além disso, o relatório final deverá poder ser gerado em duas versões: simples e completa.

---

### Requisitos obrigatórios:

#### 1 - Criar um método `generate` numa classe `SimpleReport` do módulo `inventory_report/reports/simple_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- Deve ser possível executar o método `generate` sem instanciar um objeto de `SimpleReport`
- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
   ```
- A data de validade mais próxima, somente considera itens que ainda não venceram.

**Dica**: O módulo [datetime](https://docs.python.org/3/library/datetime.html) vai te ajudar.

#### 2 - Criar um método `generate` numa classe `CompleteReport` do módulo `inventory_report/reports/complete_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- A classe `CompleteReport` deve herdar o método (`generate`) da classe `SimpleReport`, de modo a especializar seu comportamento.

- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

   Produtos estocados por empresa:
   - Physicians Total Care, Inc.: QUANTIDADE
   - Newton Laboratories, Inc.: QUANTIDADE
   - Forces of Nature: QUANTIDADE
   ```

#### 3 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo CSV o qual o caminho é passado como parâmetro.

- O método, receberá como parâmetro o caminho para o arquivo CSV e o tipo de relatório a ser gerado (`"simples"`, `"completo"`). De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

#### 4 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo JSON o qual o caminho é passado como parâmetro.

- O método, receberá como parâmetro o caminho para o arquivo JSON e o tipo de relatório a ser gerado (`"simples"`, `"completo"`). De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


#### 5 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo XML o qual o caminho é passado como parâmetro.

- O método, receberá como parâmetro o caminho para o arquivo XML e o tipo de relatório a ser gerado (`"simples"`, `"completo"`). De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

#### 6 - Criar uma classe abstrata `Importer` no módulo `inventory_report/importer/importer.py`, que terá três classes herdeiras: `CsvImporter`, `JsonImporter` e `XmlImporter`, cada uma definida em seu respectivo módulo.

- A classe abstrata deve definir a assinatura do método `import_data` a ser implementado por cada classe herdeira. Ela deve receber como parâmetro o nome do arquivo a ser importado.

- O método `import_data` definido por cada classe herdeira deve lançar uma exceção caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um  caminho de um arquivo extensão CSV para o `JsonImporter`.

- O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

#### 7 - Criar uma classe `InventoryIterator` no módulo `inventory_report/inventory/inventory_iterator.py`, que implementa a interface de um iterator (`Iterator`). A classe `InventoryRefactor` deve implementar o método `__iter__`, que retornará este iterador.

- A classe `Inventory` deverá ser refatorada (copiada) em outro arquivo chamado `inventory_report/inventory/inventory_refactor.py`. Nesse arquivo você irá refatorar a classe `Inventory` chamando-a de `InventoryRefactor`.

- A classe `InventoryRefactor` deve utilizar as classes definidas no requisito 6 para lidar com a lógica de importação, via **composição** no método `import_data`.

- A classe `InventoryRefactor` deve receber por seu construtor a classe que será utilizada para lidar com a lógica de importação e armazenar em um atributo chamado `importer`.

- As classes `InventoryIterator` e `InventoryRefactor` devem implementar corretamente a interface do padrão de projeto **Iterator**, de modo que seja possível iterar sobre os itens em estoque.

- Ao importar os dados, os mesmos devem ser armazenados na instância, em adição aos itens já presentes naquela instância. O atributo de `InventoryRefactor` que armazena esses dados deve se chamar `data`.

- Os atributos e os métodos devem ser públicos.

✍️  Para testar manualmente você pode fazer:

```python
iterator = iter(inventory)
first_item = next(iterator)
```

#### 8 - Preencha a função `main` no módulo `inventory_report/main.py` que, ao receber pela linha de comando o caminho de um arquivo e o tipo de relatório, devolve o relatório correto.

- Deverá ser usado a classe `InventoryRefactor` para recuperar os dados e gerar o relatório.

- Ao chamar o comando no formato abaixo pelo terminal, deve ser impresso na tela o devido relatório no formato da saída dos requisitos `1` e `2`: 

```bash
$ inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```

- Caso a chamada tenha menos de três argumentos (o nome `inventory_report` é considerado o primeiro argumento), exiba a mensagem de erro "Verifique os argumentos" na `stderr`.

📌 A função `sys.argv` deve ser utilizada para receber a entrada de dados da pessoa usuária.

✍️  Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `inventory_report parametro_1 parametro_2`, assim você conseguirá interagir com o menu.
