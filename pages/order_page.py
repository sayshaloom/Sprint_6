import allure
from dataclasses import field
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage # Добавили импорт базовой страницы
from locators import OrderPageLocators

class OrderPage(BasePage):
    # Конструктор __init__ удалён — он теперь автоматически наследуется из BasePage!

    @allure.step("Ввести имя")
    def set_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step("Ввести фамилию")
    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Ввести адрес")
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_SELECTOR))
        field.click()

        locator = (By.XPATH, f'//div[contains(@class, "Order_Text") and text()="{station_name}"]')
        station_item = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", station_item)
        station_item.click()

    @allure.step("Ввести номер телефона")
    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone_number)

    @allure.step("Кликнуть кнопку 'Далее'")
    def click_next_button(self):
        next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()

    @allure.step("Выбрать дату доставки самоката: {date_str}")
    def select_delivery_date(self, date_str: str):
        target_date = datetime.strptime(date_str, "%d.%m.%Y")
        target_day = str(target_date.day)
        target_month_label = target_date.strftime("month %Y-%m")

        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DELIVERY_DATE_SELECTOR))
        field.click()

        while True:
            month_element = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.CALENDAR_MONTH))
            current_month_label = month_element.get_attribute("aria-label")

            if current_month_label.replace(" ", "") == target_month_label.replace(" ", ""):
                break
            next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_MONTH_BUTTON))
            next_button.click()

        day_locator = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month")) and text()="{target_day}"]')
        day_element = self.wait.until(EC.element_to_be_clickable(day_locator))
        day_element.click()

    @allure.step("Выбрать срок аренды: {period}")
    def set_rental_period(self, period):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_SELECTOR))
        field.click()

        period_locator = (By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{period}"]')
        period_item = self.wait.until(EC.element_to_be_clickable(period_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", period_item)
        period_item.click()

    @allure.step("Выбрать цвет самоката: {color}")
    def select_scooter_color(self, color):
        if color.lower() == "black":
            checkbox = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BLACK_CHECKBOX))
        elif color.lower() == "grey":
            checkbox = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.GREY_CHECKBOX))
        checkbox.click()    

    @allure.step("Ввести комментарий для курьера")
    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    @allure.step("Кликнуть кнопку 'Заказать'")
    def click_order_button(self):
        order_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        order_button.click()

    @allure.step("Кликнуть кнопку 'Да' в окне подтверждения заказа")
    def click_confirm_button(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        confirm_button.click()

    @allure.step("Проверить появление всплывающего окна об успешном заказе")
    def is_order_successful(self):
        try:
            success_text = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_TEXT))
            return success_text.is_displayed()
        except:
            return False