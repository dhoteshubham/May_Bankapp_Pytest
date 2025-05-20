from selenium.webdriver.common.by import By


class SignUp_Class:
    text_username_xpath = "//input[@id='username']"
    text_password_xpath = "//input[@id='password']"
    text_email_xpath = "//input[@id='email']"
    text_phone_xpath = "//input[@id='phone']"
    click_create_user_button_xpath = "//button[@id='createUserButton']"
    success_message_xpath = "//div[@id='successMessage']"

    def __init__(self,driver):
        self.driver = driver

    def EnterUserName(self, name):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(name)

    def EnterPassword(self,password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def EnterEmail(self,email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def EnterPhone(self,phone):
        self.driver.find_element(By.XPATH, self.text_phone_xpath).send_keys(phone)

    def ClickCreateUserButton(self):
        self.driver.find_element(By.XPATH, self.click_create_user_button_xpath).click()

    def Verify_SuccessMessage(self):
        try:
            msg = self.driver.find_element(By.XPATH, self.success_message_xpath)
            print(msg.text)
            return "CreateUser_Pass"
        except:
            return "CreateUser_Fail"