from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FaqPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_question(self, question_locator):
        element = self.wait.until(EC.presence_of_element_located(question_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element = self.wait.until(EC.element_to_be_clickable(question_locator))
        element.click()

    def get_answer_text(self, answer_locator):
        answer = self.wait.until(EC.presence_of_element_located(answer_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", answer)
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text