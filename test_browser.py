from selene import browser, be, have


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_fail():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('439p8th0394guijnerpwoighnjsr;edofjhkbn').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))