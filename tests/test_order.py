import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import URL, order_data_1, order_data_2

class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("entry_point, order_data", [
        ("top", order_data_1),
        ("bottom", order_data_2),
    ])
    def test_order_scenario(self, driver, entry_point, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        if entry_point == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.set_first_name(order_data["first_name"])
        order_page.set_last_name(order_data["last_name"])
        order_page.set_address(order_data["address"])
        order_page.select_metro_station(order_data["metro"])
        order_page.set_phone_number(order_data["phone"])
        order_page.click_next_button()

        order_page.select_delivery_date(order_data["date"])
        order_page.set_rental_period(order_data["rent_duration"])
        order_page.select_scooter_color(order_data["color"])
        order_page.set_comment(order_data["comment"])

        order_page.click_order_button()
        order_page.click_confirm_button()

        assert order_page.is_order_successful(), "Сообщение об успешном заказе не появилось"

    @allure.title("Проверка возврата на главную страницу через логотип 'Самокат'")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_top_order_button()
        main_page.click_scooter_logo()
        main_page.wait_for_main_page_url(URL)
        
        assert main_page.get_current_url() == URL

    @allure.title("Проверка редиректа на Дзен при клике на логотип 'Яндекс'")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)

        main_window = main_page.get_current_window()
        main_page.click_yandex_logo()

        main_page.switch_to_new_tab(main_window)

        main_page.wait_for_dzen_url()

        assert "dzen.ru" in main_page.get_current_url()