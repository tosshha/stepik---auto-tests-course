import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ec,fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if (user_language == "es"):
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    if (user_language == "fr"):
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
