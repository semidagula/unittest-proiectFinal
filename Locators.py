from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.XPATH, '//*[@title="Logare"]')
ADRESA_EMAIL = (By.XPATH, '//*[@id="email"]')
PAROLA = (By.XPATH, '//*[@id="pass"]')
LOGGARE_BTN = (By.XPATH, "//*[@title='Logare']")
LOGARE_BTN = (By.XPATH,"//span[contains(text(),'Logare')]")
EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, "#advice-validate-email-email")
ERROR_LOGIN = (By.XPATH, "//div[@id='advice-validate-password-pass']")
LOGO_HOME_PAGE = (By.CSS_SELECTOR, "img[alt='Shine Boutique']")
SEARCH_BAR = (By.CSS_SELECTOR, "#search")

MARIMEA = (By.XPATH, "//span[@class='swatch-label']")

ERROARE_CAUTARE = (By.XPATH, "//p[@class='note-msg']")
SEARCHING_BTN = (By.XPATH, "//button[@title='Căutare']//i[@class='icon-search']")

MOCASINI = (By.XPATH, "//img[@id='product-collection-image-49320']")
PRET = (By.XPATH,"//span[@id='product-price-49320']//span[@class='price'][normalize-space()='229,00 RON']")
