from Pages.Basepage import Basepage
from selenium.webdriver.common.by import By

from config.config import TestData

class Registration_and_Login_Page(Basepage):

    NAME = (By.XPATH , "//input[@type = 'text']")
    EMAIL_ID = (By.XPATH, "//input[@data-qa = 'signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa = 'signup-button']")
    SIGNUP_TITLE = (By.XPATH, "//h2[text() = 'New User Signup!']")
    SIGIN_TITLE = (By.XPATH, "//div[@class = 'login-form']//h2")
    LOGIN_SIGNUP_PAGE_OPTION = (By.XPATH, "//a[@href = '/login']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_headings(self, text):
        return self.get_text(text)
    
    def do_signup(self, username, email):
        self.do_send_keys(self.NAME, username)
        self.do_send_keys(self.EMAIL_ID, email)
        self.do_click(self.SIGNUP_BUTTON)