import time
from coin import Coin, Aside
from mk_driver import IframeMk
# import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import os

load_dotenv()

# file = pandas.read_csv('imobilizados.csv')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(os.getenv('URL'))
wdw = WebDriverWait(driver, 20)
mouse = ActionChains(driver)
tela = IframeMk(
    user_name=os.getenv('USERNAME'),
    user_senha=os.getenv('PASSWORD'),
    driver=driver,
    wdw=wdw
)

tela.login()

tela.iframeCoin()
mouse.move_to_element(driver.find_element(
    By.XPATH, Coin.FINANCEIRO['xpath'])).pause(5).click().pause(5).perform()

tela.minimizeChat()

tela.iframeAsideCoin(Coin.FINANCEIRO)
mouse.move_to_element(driver.find_element(
    By.XPATH, Aside.Financeiro.GERENCIADOR_DE_CONTAS_A_RECEBER['xpath'])).pause(5).click().pause(5).perform()

tela.iframePainel(
    coin=Coin.FINANCEIRO,
    aside=Aside.Financeiro.GERENCIADOR_DE_CONTAS_A_RECEBER
)
mouse.move_to_element(driver.find_element(
    By.XPATH, '//button[@title="Envio em massa de boletos."]')).pause(5).click().pause(5).perform()

mouse.move_to_element(driver.find_element(
    By.XPATH, '//button[@title="Adicionar lote de boletos."]')).pause(5).click().pause(5).perform()

tela.iframeForm()
mouse.move_to_element(driver.find_element(
    By.XPATH, '//*[@title="Selecione a profile desejada."]/div/button')).pause(5).click().pause(5).perform()

mouse.move_to_element(driver.find_element(
    By.XPATH, '//option[@value="588"]')).pause(2).click().pause(2).perform()

mouse.move_to_element(driver.find_element(
    By.XPATH, '//*[@title="Data de vencimento inicial da pesquisa."]')).pause(2).click().send_keys('25042023').pause(2).perform()

mouse.move_to_element(driver.find_element(
    By.XPATH, '//*[@title="Data de vencimento final da pesquisa."]')).pause(2).click().send_keys('25042023').pause(2).perform()

mouse.move_to_element(driver.find_element(
    By.XPATH, '//*[@title="Marque caso deseje aplicar o filtro."]')).pause(2).click().pause(2).perform()

time.sleep(15)

tela.close()
