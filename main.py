import time
import pandas
import multiprocessing
from coin.coin import Estoque
from aside.asideEstoque import EstoqueHome
from mk_driver import Mk
from dotenv import load_dotenv
import os

load_dotenv()


def cadastroProduto(
        descricao,
        categoria,
        und,
        inativo,
        trabalho,
        serial,
        mobile
):
    instance = Mk(
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        url=os.getenv('URL'),
    )
    estoque = Estoque()
    estoqueHome = EstoqueHome()

    instance.login()

    instance.iframeCoin()
    instance.click(estoque.xpath())

    instance.minimizeChat()

    instance.iframePainel(coin=estoque, aside=estoqueHome)
    instance.click('//button[@title="Novo Produto"]')

    instance.iframeForm()
    instance.write(
        xpath='//input[@title="Informe uma breve descrição para o produto"]',
        text=descricao
    )
    instance.click(
        '//div[@title="Informe a unidade de comercialização do produto"]/div/button')

    print(descricao,
          categoria,
          und,
          inativo,
          trabalho,
          serial,
          mobile)
    time.sleep(10)
    instance.close()
    return descricao

# cadastroProduto(
#     'TAMPA 3 POSTO SEPARADOS 4X2(A.4)',
#     'INFRAESTRUTURA DE REDE EXTERNA  ',
#     'KIT',
#     'Não',
#     'Não',
#     'Não',
#     'Sim'
# )


fileProduto = pandas.read_excel('estoque.xlsx')
lista = []

for i in fileProduto.iterrows():
    lista.append((
        i[1]['PRODUTOS'],
        i[1]['CATEGORIAS'],
        i[1]['UND'],
        i[1]['INATIVO'],
        i[1]['TRABALHO'],
        i[1]['SERIAL'],
        i[1]['MOBILE']
    ))

# lista = [i for i in range(20)]

# número de processos a serem criados
num_processes = multiprocessing.cpu_count()

# cria um pool com o número de processos obtidos
pool = multiprocessing.Pool(processes=num_processes-2)

# executa a função minha_funcao para cada cliente na lista em paralelo
resultados = []
for item in lista:
    resultados.append(pool.apply_async(cadastroProduto, args=item))

# obtém os resultados de cada processo e os armazena em uma lista
resultados = [r.get() for r in resultados]

# exibe os resultados
# print(resultados)
