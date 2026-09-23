from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def accept_cookies(self):
        try:
            button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON))
            button.click()
        except TimeoutException:
            # баннер cookies не появился — значит, либо уже принят, либо не показан в этот раз
            pass

    def click_top_order_button(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.TOP_ORDER_BUTTON))
        button.click()

    def click_bottom_order_button(self):
        # сначала находим кнопку (даже если она не видна на экране — в DOM она уже есть)
        button = self.wait.until(EC.presence_of_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON))
        
        # скроллим до неё
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        
        # теперь ждём, что она стала кликабельной (видимой и активной) — и кликаем
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        button.click()

    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO))
        logo.click()

    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO))
        logo.click()