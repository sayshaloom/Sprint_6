import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Принять куки (если баннер появился)")
    def accept_cookies(self):
        self.click_safe(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Кликнуть по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Дождаться возврата на главную страницу")
    def wait_for_main_page_url(self, url):
        self.wait_for_url(url)

    @allure.step("Дождаться перехода на Дзен")
    def wait_for_dzen_url(self):
        self.wait_for_url_contains("dzen.ru")