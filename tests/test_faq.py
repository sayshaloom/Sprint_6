import pytest
from locators import FaqLocators
from pages.faq_page import FaqPage
from pages.main_page import MainPage
import data


class TestFaq:

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (FaqLocators.QUESTION_1, FaqLocators.ANSWER_1, data.FAQ_ANSWER_1),
            (FaqLocators.QUESTION_2, FaqLocators.ANSWER_2, data.FAQ_ANSWER_2),
            (FaqLocators.QUESTION_3, FaqLocators.ANSWER_3, data.FAQ_ANSWER_3),
            (FaqLocators.QUESTION_4, FaqLocators.ANSWER_4, data.FAQ_ANSWER_4),
            (FaqLocators.QUESTION_5, FaqLocators.ANSWER_5, data.FAQ_ANSWER_5),
            (FaqLocators.QUESTION_6, FaqLocators.ANSWER_6, data.FAQ_ANSWER_6),
            (FaqLocators.QUESTION_7, FaqLocators.ANSWER_7, data.FAQ_ANSWER_7),
            (FaqLocators.QUESTION_8, FaqLocators.ANSWER_8, data.FAQ_ANSWER_8),
        ]
    )
    def test_faq_answer_appears(self, driver, question_locator, answer_locator, expected_text):
        driver.get(data.URL)

        main_page = MainPage(driver)
        main_page.accept_cookies()

        faq_page = FaqPage(driver)
        faq_page.click_question(question_locator)
        actual_text = faq_page.get_answer_text(answer_locator)

        assert actual_text.strip() == expected_text.strip()