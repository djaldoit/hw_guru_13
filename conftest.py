import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    print(f'Window size: {browser.config.window_width}x{browser.config.window_height}')
    yield
    browser.quit()
