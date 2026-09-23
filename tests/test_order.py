import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import URL, order_data_1, order_data_2


class TestOrder:

    @pytest.mark.parametrize("entry_point, order_data", [
        ("top", order_data_1),
        ("bottom", order_data_2),
    ])
    def test_order_scenario(self, driver, entry_point, order_data):
        driver.get(URL)

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # 0. принимаем куки
        main_page.accept_cookies()

        # 1. нажимаем кнопку "Заказать" — верхнюю или нижнюю, в зависимости от параметра
        if entry_point == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        # 2. заполняем первую часть формы (имя, фамилия, адрес, станция метро, телефон)
        order_page.set_first_name(order_data["first_name"])
        order_page.set_last_name(order_data["last_name"])
        order_page.set_address(order_data["address"])
        order_page.select_metro_station(order_data["metro"])
        order_page.set_phone_number(order_data["phone"])
        order_page.click_next_button()

        # 3. заполняем вторую часть формы (дата, срок аренды, цвет, комментарий)
        order_page.select_delivery_date(order_data["date"])
        order_page.set_rental_period(order_data["rent_duration"])
        order_page.select_scooter_color(order_data["color"])
        order_page.set_comment(order_data["comment"])

        # 4. оформляем заказ и подтверждаем
        order_page.click_order_button()
        order_page.click_confirm_button()

        # 5. проверяем, что заказ оформлен успешно
        assert order_page.is_order_successful(), "Сообщение об успешном заказе не появилось"

    def test_scooter_logo_redirects_to_main_page(self, driver):
        driver.get(URL)

        main_page = MainPage(driver)
        main_page.accept_cookies()

        # уходим с главной страницы, чтобы клик по логотипу был проверяемым действием
        main_page.click_top_order_button()
        assert driver.current_url != URL, "Не удалось уйти с главной страницы для проверки"

        # кликаем по логотипу самоката
        main_page.click_scooter_logo()

        # проверяем, что вернулись на главную
        WebDriverWait(driver, 10).until(EC.url_to_be(URL))
        assert driver.current_url == URL

    def test_yandex_logo_redirects_to_dzen(self, driver):
        driver.get(URL)

        main_page = MainPage(driver)
        main_page.accept_cookies()

        main_window = driver.current_window_handle
        main_page.click_yandex_logo()

        # ждём, пока откроется вторая вкладка
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        new_window = [window for window in all_windows if window != main_window][0]
        driver.switch_to.window(new_window)

        # ждём, пока в новой вкладке загрузится Дзен
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url