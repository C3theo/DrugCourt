from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.chrome.service as service
from behave import fixture, use_fixture
import time


@fixture
def browser_chrome(context):

    # chrome_service = service.Service(
    #     'C:\\Users\\TheoI\\OneDrive\\Documents\\Projects\\Python\\Drug Court\\Browser Drivers\\chromedriver_win32\\chromedriver.exe')
    # chrome_service.start()
    # capabilities = {
    #     'chrome.binary': "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"}
    # driver = webdriver.Remote(chrome_service.service_url, capabilities)
    # options = webdriver.ChromeOptions()
    # context.browser = driver
    context.browser = webdriver.Chrome()
    # options='--no-sandbox'
    context.browser.set_page_load_timeout(60)
    yield context.browser
    context.browser.quit()
    time.sleep(0.5)


def before_all(context):
    # use_fixture(browser_chrome, context)
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    context.browser.set_page_load_timeout(60)


def after_all(context):

    context.browser.quit()
    time.sleep(0.5)


def before_feature(context, feature):
    pass
