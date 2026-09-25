from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        # ожидание для баннера cookie
        self.short_wait = WebDriverWait(self.driver, 5)

    @staticmethod
    def _scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self._scroll_into_view(self.driver, element)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # метод для cookie
    def click_safe(self, locator):
        try:
            element = self.short_wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            pass

    # метод для поиска элемента при выборе даты доставки
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def type_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    # метод для получения текста ответа из Вопросов о важном
    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self._scroll_into_view(self.driver, element)
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    # метод для проверки, что появилось сообщение об успешно оформленном заказе
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    # метод для теста на открытие новой вкладки
    def get_current_window(self):
        return self.driver.current_window_handle        

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    # метод для проверки url Яндекс Дзен
    def wait_for_url_contains(self, substring):
        self.wait.until(EC.url_contains(substring))

    def switch_to_new_tab(self, old_window):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = [w for w in self.driver.window_handles if w != old_window][0]
        self.driver.switch_to.window(new_window)     
