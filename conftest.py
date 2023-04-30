import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import FirefoxProfile

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default=None, help="Choose language: es/en/ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
  

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = FirefoxProfile()
        options_firefox.set_preference('intl.accept_languages', user_language)
        options_firefox.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

