import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Class
from utilities.Logger_utility import logger_class
from utilities.additional_utilities import additional_Utilities_class
from utilities.readConfig_utility import ReadConfig_class


# step 1
# @pytest.fixture()
# def setup():
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser",default = "chrome")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_value = request.config.getoption("--browser")
    if browser_value == "chrome":
        print("launching Chrome browser")
        driver = webdriver.Chrome()
    elif browser_value == "firefox":
        print("launching Firefox browser")
        driver = webdriver.Firefox()
    elif browser_value == "edge":
        print("launching Edge browser")
        driver = webdriver.Edge()
    elif browser_value == "headless":
        print("launching Headless Chrome browser")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    # else:
    #     print("launching Chrome browser as default")
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Attaching browser driver object to class
    request.cls.driver = driver
    yield driver
    driver.quit()


username = ReadConfig_class.username_data()
password = ReadConfig_class.password_data()
base_url = ReadConfig_class.base_url()
login_url = ReadConfig_class.login_url()
signup_url = ReadConfig_class.signup_url()
log = logger_class.log_gen_method()
@pytest.fixture
def bankapp_login(setup):
    log.info(f"Opening the Bank Application URL: {base_url}")
    # Initialize the test case
    driver.get(login_url)
    # Enter the Username & Password
    lp = Login_Class(driver)
    log.info(f"Enter the Username: {username}")
    lp.EnterUserName(username)
    log.info(f"Enter the Password: {password}")
    lp.EnterPassword(password)
    log.info(f"Click the Login Button")
    additional_Utilities_class.explicit_wait(driver, (By.XPATH, lp.click_login_button_xpath), 10)
    lp.ClickLoginButton()

