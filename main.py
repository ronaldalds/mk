import time
import multiprocessing
from coin.coin import Crm
from aside.asideCrm import GerenciadorDeFechamento
from mk_driver import Mk
from dotenv import load_dotenv
import os

load_dotenv()


def sendEmail(num) -> int:
    crm = Crm()
    gdf = GerenciadorDeFechamento()
    instance = Mk(
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        url=os.getenv('URL'),
    )

    instance.login()

    instance.iframeCoin()
    instance.click(crm.xpath())

    instance.iframeAsideCoin(crm)
    instance.click(gdf.xpath())

    print(num)
    time.sleep(10)
    instance.close()
    return num


lista_de_clientes = [i for i in range(50)]

# número de processos a serem criados
num_processes = multiprocessing.cpu_count()

# cria um pool com o número de processos obtidos
pool = multiprocessing.Pool(processes=num_processes-1)

# executa a função minha_funcao para cada cliente na lista em paralelo
resultados = []
for cliente in lista_de_clientes:
    # print(cliente)
    resultados.append(pool.apply_async(sendEmail, args=(cliente,)))

# obtém os resultados de cada processo e os armazena em uma lista
resultados = [r.get() for r in resultados]

# exibe os resultados
print(resultados)
