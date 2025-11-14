from random import choices

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chrome",choices = ['chrome', 'webkit', 'firefox'],
                     help="Type in the browser name")


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

# request is the global parameter that is provided by pytest which will check the
# parameter that is passed to the fixture in global level env variables and local variables in that test case
# and will return the value of that parameter to the fixture function

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser-name")
    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'webkit':
        browser = playwright.webkit.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page
    context.close()
    browser.close()