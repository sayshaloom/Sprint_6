import allure
from pages.base_page import BasePage

class FaqPage(BasePage):

    @allure.step("Нажать на стрелочку вопроса в FAQ")
    def click_question(self, question_locator):
        self.click(question_locator)

    @allure.step("Получить текст открывшегося ответа в FAQ")
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)