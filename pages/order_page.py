import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Ввести имя")
    def set_first_name(self, first_name):
        self.type_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step("Ввести фамилию")
    def set_last_name(self, last_name):
        self.type_text(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Ввести адрес")
    def set_address(self, address):
        self.type_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        self.click(OrderPageLocators.METRO_STATION_SELECTOR)
        locator = (By.XPATH, f'//div[contains(@class, "Order_Text") and text()="{station_name}"]')
        self.click(locator)

    @allure.step("Ввести номер телефона")
    def set_phone_number(self, phone_number):
        self.type_text(OrderPageLocators.PHONE_INPUT, phone_number)

    @allure.step("Кликнуть кнопку 'Далее'")
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки самоката: {date_str}")
    def select_delivery_date(self, date_str: str):
        target_date = datetime.strptime(date_str, "%d.%m.%Y")
        target_day = str(target_date.day)
        target_month_label = target_date.strftime("month %Y-%m")

        self.click(OrderPageLocators.DELIVERY_DATE_SELECTOR)

        while True:
            month_element = self.find(OrderPageLocators.CALENDAR_MONTH)
            current_month_label = month_element.get_attribute("aria-label")

            if current_month_label.replace(" ", "") == target_month_label.replace(" ", ""):
                break
            self.click(OrderPageLocators.NEXT_MONTH_BUTTON)

        day_locator = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month")) and text()="{target_day}"]')
        self.click(day_locator)

    @allure.step("Выбрать срок аренды: {period}")
    def set_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD_SELECTOR)
        period_locator = (By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{period}"]')
        self.click(period_locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_scooter_color(self, color):
        if color.lower() == "black":
            self.click(OrderPageLocators.BLACK_CHECKBOX)
        elif color.lower() == "grey":
            self.click(OrderPageLocators.GREY_CHECKBOX)    

    @allure.step("Ввести комментарий для курьера")
    def set_comment(self, comment):
        self.type_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Кликнуть кнопку 'Заказать'")
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть кнопку 'Да' в окне подтверждения заказа")
    def click_confirm_button(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить появление всплывающего окна об успешном заказе")
    def is_order_successful(self):
        return self.is_visible(OrderPageLocators.SUCCESS_TEXT)