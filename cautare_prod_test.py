import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from ProiectUnittestShein import Locators
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCautareProduse(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://shine-boutique.ro/')
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.MARIMEA))
        self.assertTrue(Locators.PRET, "229,00 RON")

    def test6_cautare_invalida(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys("excavator")
        self.driver.find_element(*Locators.SEARCHING_BTN).click()
        expected_result = "Căutarea dvs. nu a returnat niciun rezultat."
        actual_result = self.driver.find_element(*Locators.ERROARE_CAUTARE)
        self.assertTrue(expected_result, actual_result)
