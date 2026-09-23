from dataclasses import field
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def set_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    def select_metro_station(self, station_name):
        # кликаем по полю, чтобы раскрылся список
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_SELECTOR))
        field.click()

        # ищем нужную станцию в раскрывшемся списке
        locator = (By.XPATH, f'//div[contains(@class, "Order_Text") and text()="{station_name}"]')
        station_item = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", station_item)
        station_item.click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone_number)

    def click_next_button(self):
        next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()

    def select_delivery_date(self, date_str: str):
        target_date = datetime.strptime(date_str, "%d.%m.%Y")
        target_day = str(target_date.day)
        target_month_label = target_date.strftime("month %Y-%m")

        # 1. открываем календарь
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DELIVERY_DATE_SELECTOR))
        field.click()

        # 2. листаем месяцы вперёд, пока не найдём нужный
        while True:
            month_element = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.CALENDAR_MONTH))
            current_month_label = month_element.get_attribute("aria-label")

            if current_month_label.replace(" ", "") == target_month_label.replace(" ", ""):
                break
            next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_MONTH_BUTTON))
            next_button.click()

        # 3. кликаем нужный день (исключая дни из соседних месяцев)
        day_locator = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month")) and text()="{target_day}"]')
        day_element = self.wait.until(EC.element_to_be_clickable(day_locator))
        day_element.click()

    def set_rental_period(self, period):
        # кликаем по полю, чтобы раскрылся список
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_SELECTOR))
        field.click()

        # ищем нужный период в раскрывшемся списке
        period_locator = (By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{period}"]')
        period_item = self.wait.until(EC.element_to_be_clickable(period_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", period_item)
        period_item.click()

    def select_scooter_color(self, color):
        if color.lower() == "black":
            checkbox = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BLACK_CHECKBOX))
        elif color.lower() == "grey":
            checkbox = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.GREY_CHECKBOX))
        checkbox.click()    

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    def click_order_button(self):
        order_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        order_button.click()

    def click_confirm_button(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        confirm_button.click()

    def is_order_successful(self):
        try:
            success_text = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_TEXT))
            return success_text.is_displayed()
        except:
            return False

                     


            

