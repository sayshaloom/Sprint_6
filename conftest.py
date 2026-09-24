import pytest
from selenium import webdriver
from pages.main_page import MainPage
from data import URL

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    
    # Перенесли повторяющиеся шаги из начала тестов сюда:
    browser.get(URL)
    main_page = MainPage(browser)
    main_page.accept_cookies()
    
    yield browser
    browser.quit()