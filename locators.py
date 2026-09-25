from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")

class OrderPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_SELECTOR = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    DELIVERY_DATE_SELECTOR = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    CALENDAR_MONTH = (By.CLASS_NAME, "react-datepicker__month")
    NEXT_MONTH_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Next Month"]')
    RENTAL_PERIOD_SELECTOR = (By.XPATH, ".//div[text()='* Срок аренды']")
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_BUTTON =(By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_TEXT = (By.XPATH, ".//div[text()='Заказ оформлен']")

class FaqLocators:
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")

    ANSWER_1 = (By.ID, "accordion__panel-0")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    ANSWER_8 = (By.ID, "accordion__panel-7")    