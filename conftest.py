import pytest

from selene import browser

@pytest.fixture (scope="session")
def browser_size():
    browser.config.driver_name = "chrome"
    browser.config.window_height = 1000
    browser.config.window_width = 750

@pytest.fixture(autouse=True)
def open_browser_with_message():
    browser.open("https://google.com")

    yield

    print("Поиск не выдает результата.")