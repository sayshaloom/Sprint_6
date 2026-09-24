import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    # __init__ удален, так как он автоматически наследуется из BasePage

    @allure.step("Принять куки (если баннер появился)")
    def accept_cookies(self):
        try:
            button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON))
            button.click()
        except TimeoutException:
            pass

    @allure.step("Кликнуть по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.TOP_ORDER_BUTTON))
        button.click()

    @allure.step("Кликнуть по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        button = self.wait.until(EC.presence_of_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        button.click()

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO))
        logo.click()

    @allure.step("Кликнуть по логотипу Яндекс")
    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO))
        logo.click()