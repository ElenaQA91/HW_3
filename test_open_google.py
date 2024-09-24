from selene import browser, be, have


def test_open_brawser():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_unsuccessful_brawser():
    text = '868689698^%&%&%^&*'
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('.card-section').should(have.text(f"По запросу {text} ничего не найдено"))