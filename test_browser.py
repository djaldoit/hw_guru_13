from selene import browser, be, have
import pytest


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_filed_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('pivo po akcii').press_enter()
    browser.element('[id="search"]').should(have.text('asdfasdfasdf'))
