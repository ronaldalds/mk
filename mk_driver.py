import time
from coin import Coin, Aside
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable,
    alert_is_present
)


class IframeMk:
    def __init__(self, user_name: str, user_senha: str, driver: WebDriver, wdw: WebDriverWait):
        self.user_name = user_name
        self.user_senha = user_senha
        self.driver = driver
        self.wdw = wdw

    def login(self):
        self.driver.find_element(
            By.XPATH, '//input[@placeholder="Nome do usuário"]').send_keys(self.user_name)
        self.driver.find_element(
            By.XPATH, '//input[@placeholder="Senha"]').send_keys(self.user_senha)
        self.driver.find_element(By.XPATH, '//button[@name="user"]').click()

    def minimizeChat(self):
        self.driver.switch_to.default_content()
        self.iframeMain()
        self.wdw.until(element_to_be_clickable(
            (By.XPATH, '//*[@id="jsxc_toggleRoster"]')))
        self.driver.find_element(
            By.XPATH, '//*[@id="jsxc_toggleRoster"]').click()

    def close(self):
        self.driver.close()

    def iframeMain(self):
        self.driver.switch_to.default_content()
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//frame[@name="mainsystem"]')))
        return self

    def iframeCoin(self):
        self.driver.switch_to.default_content()
        self.iframeMain()
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))
        return self

    def iframeForm(self):
        self.driver.switch_to.default_content()
        self.iframeMain()
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//*[@class="FormIframe"]/iframe')))
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))

    def iframeAsideCoin(self, coin: dict):
        self.driver.switch_to.default_content()
        self.iframeCoin()
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, f'//iframe[@componenteaba="{coin["title"]} - PainelCloseAbaPrincipal"]')))
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))
        return self

    def iframePainel(self, coin: dict, aside: dict):
        self.driver.switch_to.default_content()
        self.iframeAsideCoin(coin)
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, f'//iframe[@componenteaba="{aside["title"]}ClosePainelAba"]')))
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))
        return self

    def iframeGrid(self, coin: dict, aside: dict):
        self.driver.switch_to.default_content()
        self.iframePainel(coin, aside)
        self.wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//div[@id="lay"]/div[2]/div[2]/div[1]/div/iframe')))
        return self
