from Pages.Basepage import Basepage
from selenium.webdriver.common.by import By

from config.config import TestData

class Registration_and_Login_Page(Basepage):

    NAME = (By.XPATH , "//input[@type = 'text']")
    EMAIL_ID = (By.XPATH, "//input[@data-qa = 'signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa = 'signup-button']")
    SIGNUP_TITLE = (By.XPATH, "//h2[text() = 'New User Signup!']")
    SIGNIN_TITLE = (By.XPATH, "//div[@class = 'login-form']//h2")
    LOGIN_SIGNUP_PAGE_OPTION = (By.XPATH, "//a[@href = '/login']")
    LOGIN_EMAILFIELD = (By.XPATH, "//input[@data-qa = 'login-email']")
    LOGIN_PASSWORDFIELD = (By.XPATH, "//input[@data-qa = 'login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa = 'login-button']")
    LOGIN_PLACEHOLDER = (By.XPATH, "//form[@action = '/login']//input[@placeholder = 'Email Address']")
    LOGIN_PASSWORD_PLACEHOLDER = (By.XPATH, "//form[@action = '/login']//input[@placeholder = 'Password']")
    SIGNUP_NAME_PLACEHOLDER = (By.XPATH, "//form[@action = '/signup']//input[@placeholder = 'Name']")
    SIGNUP_EMAIL_PLACEHOLDER = (By.XPATH, "//form[@action = '/signup']//input[@placeholder = 'Email Address']")
    LOGO = (By.XPATH, "//a//img")
    PAGE_TITLE = (By.XPATH, "//title")
    OR_text = (By.XPATH, "//h2[contains(text(), 'OR')]")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_headings(self, locator):
        heading = self.get_text(locator)
        return heading
    
    def do_signup(self, username, email):
        self.do_send_keys(self.NAME, username)
        self.do_send_keys(self.EMAIL_ID, email)
        self.do_click(self.SIGNUP_BUTTON)

    def do_login(self, email, password):
        self.do_send_keys(self.LOGIN_EMAILFIELD, email)
        self.do_send_keys(self.LOGIN_PASSWORDFIELD, password)
        self.do_click(self.LOGIN_BUTTON)

    def get_pagetitle(self):
        return self.get_title(self.PAGE_TITLE)
    
    def find_loginfields(self):
        email_field_found = self.findelement(self.LOGIN_EMAILFIELD)
        password_field_found = self.findelement(self.LOGIN_PASSWORDFIELD)
        return email_field_found and password_field_found
    
    def login_placeholders(self):
        email_placeholder = self.findelement(self.LOGIN_PLACEHOLDER)
        password_placeholder = self.findelement(self.LOGIN_PASSWORD_PLACEHOLDER)
        return email_placeholder and password_placeholder
    
    def find_login_button(self):
        return self.findelement(self.LOGIN_BUTTON)
    
    def find_signupfields(self):
        username_field = self.findelement(self.NAME)
        emailid_field = self.findelement(self.EMAIL_ID)
        return username_field and emailid_field
    
    def signup_placeholders(self):
        username_placeholder = self.findelement(self.SIGNUP_NAME_PLACEHOLDER)
        email_placehloder = self.findelement(self.SIGNUP_EMAIL_PLACEHOLDER)
        return username_placeholder and email_placehloder
    
    def find_signup_button(self):
        return self.findelement(self.SIGNUP_BUTTON)
    
    def find_logo(self):
        return self.findelement(self.LOGO)
    
    def find_OR_text(self):
        return self.findelement(self.find_OR_text)



        

