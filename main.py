import time
from coin import Crm, Financeiro
from asideCrm import GerenciadorDeFechamento
from mk_driver import Mk
# import pandas
from dotenv import load_dotenv
import os

load_dotenv()
crm = Crm()
gdf = GerenciadorDeFechamento()


async def pro(inta: Mk):
    inta.login()
    inta.iframeCoin()
    inta.click(crm.xpath())
    inta.minimizeChat()
    inta.iframeAsideCoin(crm)
    inta.click(gdf.xpath())
    inta.iframePainel(crm, gdf)
    inta.click(
        '//button[@title="Detalhes dos produtos (Mês corrente)"]')

# file = pandas.read_csv('imobilizados.csv')


emailSendingInvoice = Mk(
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    url=os.getenv('URL'),
)
emailSendingInvoice2 = Mk(
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    url=os.getenv('URL'),
)

pro(emailSendingInvoice)
pro(emailSendingInvoice2)


# mouse.move_to_element(driver.find_element(
#     By.XPATH, Coin.FINANCEIRO['xpath'])).pause(5).click().pause(5).perform()

# tela.minimizeChat()

# tela.iframeAsideCoin(Coin.FINANCEIRO)
# mouse.move_to_element(driver.find_element(
#     By.XPATH, Aside.Financeiro.GERENCIADOR_DE_CONTAS_A_RECEBER['xpath'])).pause(5).click().pause(5).perform()

# tela.iframePainel(
#     coin=Coin.FINANCEIRO,
#     aside=Aside.Financeiro.GERENCIADOR_DE_CONTAS_A_RECEBER
# )
# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//button[@title="Envio em massa de boletos."]')).pause(5).click().pause(5).perform()

# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//button[@title="Adicionar lote de boletos."]')).pause(5).click().pause(5).perform()

# tela.iframeForm()
# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//*[@title="Selecione a profile desejada."]/div/button')).pause(5).click().pause(5).perform()

# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//option[@value="588"]')).pause(2).click().pause(2).perform()

# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//*[@title="Data de vencimento inicial da pesquisa."]')).pause(2).click().send_keys('25042023').pause(2).perform()

# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//*[@title="Data de vencimento final da pesquisa."]')).pause(2).click().send_keys('25042023').pause(2).perform()

# mouse.move_to_element(driver.find_element(
#     By.XPATH, '//*[@title="Marque caso deseje aplicar o filtro."]')).pause(2).click().pause(2).perform()

time.sleep(15)

tela.close()
