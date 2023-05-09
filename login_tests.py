import unittest
from selenium import webdriver

import time

from ProiectUnittestShein import Locators


class TestLoginPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://shine-boutique.ro/')
        self.driver.maximize_window()
        time.sleep(2)


    def test1_get_logo(self):
        self.driver.find_element(*Locators.LOGO_HOME_PAGE).is_displayed()

    def test2_wrong_password_login(self):
        self.driver.find_element(*Locators.LOGGARE_BTN).click()
        self.driver.find_element(*Locators.ADRESA_EMAIL).send_keys("sem.gula@gmail.com")
        self.driver.find_element(*Locators.PAROLA).send_keys("123abc")
        self.driver.find_element(*Locators.LOGARE_BTN).click()

        expected_result = "Please enter more characters or clean leading or trailing spaces."
        actual_result = self.driver.find_element(*Locators.ERROR_LOGIN)
        self.assertTrue(expected_result, actual_result)

    def test3_wrong_email_login(self):
        self.driver.find_element(*Locators.LOGGARE_BTN).click()
        self.driver.find_element(*Locators.ADRESA_EMAIL).send_keys("sem.gula@gmailcom")
        self.driver.find_element(*Locators.PAROLA).send_keys("123abc")
        self.driver.find_element(*Locators.LOGARE_BTN).click()

        expected_result = "Introduceți o adresă de e-mail corectă. De exemplu ionpopescu@domeniu.ro."
        actual_result = self.driver.find_element(*Locators.EMAIL_ERROR_MESSAGE)
        self.assertTrue(expected_result, actual_result)

    def tearDown(self) -> None:
        self.driver.quit()
