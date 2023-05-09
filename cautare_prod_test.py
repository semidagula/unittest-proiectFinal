import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from ProiectUnittestShein import Locators
import unittest


class TestCautareProduse(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://shine-boutique.ro/')
        self.driver.maximize_window()
        time.sleep(2)

    def test4_cautare_produs(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys("Pantofi baieti")
        self.driver.find_element(*Locators.SEARCHING_BTN).click()
        self.driver.find_element(*Locators.MOCASINI).click()
        expected_result = "https://shine-boutique.ro/mocasini-bleumarin-baieti-mayoral-41046-mymoc01k.html#." \
                          "ZFpMbnZBznYhttps://shine-boutique.ro/mocasini-bleumarin-baieti-mayoral-41046-mymoc01k." \
                          "html#.ZFpMbnZBznY"
        actual_result = self.driver.current_url
        self.assertTrue(expected_result, actual_result)

    def test5_verificare_pret(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys("Pantofi baieti")
        self.driver.find_element(*Locators.SEARCHING_BTN).click()
        self.driver.find_element(*Locators.MOCASINI).click()
        pret = (By.XPATH, "//span[@id='product-price-49320']//span[@class='price'][normalize-space()='229,00 RON']")
        self.assertTrue(pret, "229,00 RON")

    def test6_cautare_invalida(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys("excavator")
        self.driver.find_element(*Locators.SEARCHING_BTN).click()
        time.sleep(3)
        expected_result = "Căutarea dvs. nu a returnat niciun rezultat."
        actual_result = self.driver.find_element(*Locators.ERROARE_CAUTARE)
        self.assertTrue(expected_result, actual_result)

    def tearDown(self) -> None:
        self.driver.quit()
