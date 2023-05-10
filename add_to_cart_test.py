import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from ProiectUnittestShein import Locators
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddRemoveItems(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://shine-boutique.ro/')
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test7_add_to_cart(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys("geanta")
        self.driver.find_element(*Locators.SEARCHING_BTN).click()
        self.driver.find_element(*Locators.GEANTA).click()

        # Wait for the size options to load
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.MARIMEA_UNI))
        # Click on the size option
        self.driver.find_element(*Locators.MARIMEA_UNI).click()
        # Add the product to cart
        self.driver.find_element(*Locators.ADAUGARE_IN_COS).click()
        # Assert that the product was added to cart successfully
        expected_result = "GEANTĂ PIELE ECO CU PRINT SNAKE MARO IT-GNT02Y a fost adăugat la coșul de cumpărături"
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(Locators.SUCCES_MSG_GEANTA, expected_result)))

    def test8_remove_from_cart(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys("geanta")
        self.driver.find_element(*Locators.SEARCHING_BTN).click()
        self.driver.find_element(*Locators.GEANTA).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.MARIMEA_UNI))
        # Click on the size option
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "product-view-zoom-area")))
        self.driver.find_element(*Locators.MARIMEA_UNI).click()
        self.driver.find_element(*Locators.ADAUGARE_IN_COS).click()
        self.driver.find_element(*Locators.CART).click()
        self.driver.find_element(*Locators.REMOVE_CART).click()
        expected_result = "COȘUL DE CUMPĂRĂTURI ESTE GOL"
        actual_result = self.driver.find_element(*Locators.EMPTY_CART_MSG).text
        self.assertEqual(expected_result, actual_result)
