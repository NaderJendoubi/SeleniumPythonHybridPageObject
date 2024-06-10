import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities.ReadConfigurations import ReadConfigurations

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_and_teardown(request):
    # browser = ReadConfigurations.read_configuration("basic info", "browser")
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    # print(browser)
    # print(type(browser))
    # print(request.cls)
    # print(request.cls.__dict__)
    # print(request.cls.__dict__['driver'])
    # print(request.cls.__dict__['driver'].title)
    # print(request.cls.__dict__['driver'].current_url)
    # print(request.cls.__dict__['driver'].get_screenshot_as_png())
    # print(request.cls.__dict__['driver'].get_window_size())
    # print(request.cls.__dict__['driver'].get_window_position())
    # print(request.cls.__dict__['driver'].get_window_rect())
    # print(request.cls.__dict__['driver'].get_window_handle())
    global driver
    driver = None
    if browser.__eq__("chrome"):
        # chrome_options = webdriver.ChromeOptions())
        # chrome_options.add_argument("--start-maximized")
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser.__eq__("edge"):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
