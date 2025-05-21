import time
from string import digits


import pytest
from faker.generator import random
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Class
from pageObjects.SignUp_Page import SignUp_Class
from utilities.Logger_utility import logger_class
from utilities.additional_utilities import additional_Utilities_class
from utilities.readConfig_utility import ReadConfig_class


@pytest.mark.usefixtures("setup")
class Test_Login001:
    username = ReadConfig_class.username_data()
    password = ReadConfig_class.password_data()
    base_url = ReadConfig_class.base_url()
    login_url = ReadConfig_class.login_url()
    signup_url = ReadConfig_class.signup_url()
    log = logger_class.log_gen_method()



    driver = None
    @pytest.mark.sanity
    @pytest.mark.userprofile
    @pytest.mark.xfail
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.dependency(depends=["test_bankapp_url_001"])
    def test_bankapp_url_001(self):
        self.log.info("Test Case Started: test_bankapp_url_001")
        self.log.info(f"Opening the Bank Application URL: {self.base_url}")
        self.driver.get(self.base_url)
        #Initialize the test case
        self.log.info(f"Checking the Bank Application URL: {self.driver.title}")
        # Open the application
        if self.driver.title == "Bank Application":
            print("Test Case Passed: Bank Application URL is Opened")
            self.log.info("Taking Screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_url_001_pass.png")
            additional_Utilities_class.take_screenshot(self.driver, "test_bankapp_url_001_pass", "pass")
            self.log.info("Test Case Passed: Bank Application URL is Opened\n")
            assert True
        else:
            self.log.info("Taking Screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_url_001_fail.png")
            additional_Utilities_class.take_screenshot(self.driver, "test_bankapp_url_001_fail", "fail")
            print("Test Case Failed: Bank Application URL is NOT Opened")
            self.log.info("Test Case Failed: Bank Application URL is Opened\n")
            assert False


    @pytest.mark.sanity
    @pytest.mark.userprofile
    @pytest.mark.dependency(depends=["test_bankapp_url_001"])
    def test_bankapp_login_002(self):
        self.log.info("Test Case Started: test_bankapp_login_002")
        self.log.info(f"Opening the Bank Application URL: {self.base_url}")
        #Initialize the test case
        self.driver.get(self.login_url)
        #Enter the Username & Password
        lp = Login_Class(self.driver)
        self.log.info(f"Enter the Username: {self.username}")
        lp.EnterUserName(self.username)
        self.log.info(f"Enter the Password: {self.password}")
        lp.EnterPassword(self.password)
        self.log.info(f"Click the Login Button")
        additional_Utilities_class.explicit_wait(self.driver, (By.XPATH, lp.click_login_button_xpath), 10)
        lp.ClickLoginButton()
        time.sleep(3)
        if self.driver.title == "Dashboard":
            print("Test Case Passed: Login Successful")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_login_002_pass.png")
            additional_Utilities_class.take_screenshot(self.driver, "test_bankapp_login_002_pass", "pass")
            assert True
        else:
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_login_002_fail.png")
            additional_Utilities_class.take_screenshot(self.driver, "test_bankapp_login_002_fail", "fail")
            print("Test Case Failed: Login Failed")
            assert False


    @pytest.mark.group1
    @pytest.mark.userprofile
    @pytest.mark.skip
    @pytest.mark.xfail
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.dependency(depends=["test_bankapp_url_001"])
    def test_bankapp_signup_003(self,faker):
        #Initialize the test case
        self.driver.get(self.signup_url)
        sp = SignUp_Class(self.driver)
        username = faker.name()
        sp.EnterUserName(username)
        print(f"Username: {username}")
        sp.EnterPassword("Sample@123")
        print(f"Password: Sample@123")
        email = faker.email()
        sp.EnterEmail(email)
        print(f"Email: {email}")
        phone = "".join([str(random.randint(0, 9)) for _ in range(10)])
        sp.EnterPhone(phone)
        print(f"Phone: {phone}")
        time.sleep(5)
        sp.ClickCreateUserButton()
        additional_Utilities_class.explicit_wait(self.driver, (By.XPATH, sp.success_message_xpath), 10)
        if sp.Verify_SuccessMessage() == "CreateUser_Pass":
            print("Test Case Passed: SignUp Successful")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_signup_003_pass.png")
            additional_Utilities_class.take_screenshot(self.driver, "test_bankapp_signup_003_pass", "pass")
            assert True
        else:
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_signup_003_fail.png")
            additional_Utilities_class.take_screenshot(self.driver, "test_bankapp_signup_003_fail", "fail")
            print("Test Case Failed: SignUp Failed")
            assert False



"pytest -v -s --html=Reports/my_report.html -n auto --browser chrome"
