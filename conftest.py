import pytest

from selene import browser

@pytest.fixture (scope="session")
def browser_size():
    browser.config.driver_name = "chrome"
    browser.config.window_height = 1000
    browser.config.window_width = 750