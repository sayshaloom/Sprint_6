import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FaqPage(BasePage):

    @allure.step("Нажать на стрелочку вопроса в FAQ")
    def click_question(self, question_locator):
        element = self.wait.until(EC.presence_of_element_located(question_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element = self.wait.until(EC.element_to_be_clickable(question_locator))
        element.click()

    @allure.step("Получить текст открывшегося ответа в FAQ")
    def get_answer_text(self, answer_locator):
        answer = self.wait.until(EC.presence_of_element_located(answer_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", answer)
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text