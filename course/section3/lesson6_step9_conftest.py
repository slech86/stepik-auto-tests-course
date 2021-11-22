import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()



# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default="ru",
#                      help="Choose language: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb")

# @pytest.fixture(scope="function")
# def browser(request):
#     languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb "
#     language = request.config.getoption("language")
#     if (language + " ") in languages:
#         print("\nstart chrome browser for test..")
#         options = Options()
#         options.add_experimental_option(
#             'prefs', {'intl.accept_languages': language})
#         browser = webdriver.Chrome(options=options)
#     else:
#         print("\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb".format(language))
#         pytest.fail("Wrong Language")
#         # assert 0
#     yield browser
#     print("\nquit browser...")
#     browser.quit()



# @pytest.fixture(scope="function")
# def browser(request):
#     user_language = request.config.getoption('language')
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()



# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default='ru', help="Choose locale")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     user_language = request.config.getoption("--language")
#     options = Options()
#     if user_language in ("ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "zh-hans", "uk"):
#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#         browser = webdriver.Chrome(options=options)
#     else:
#         raise pytest.UsageError(f"--language {user_language} is not supported")
#     yield browser
#     browser.quit()