from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage():

    def __init__(self,driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, user_input):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(user_input)

    def get_text(self, locator):
        Text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return Text.text
    
    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)
    
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    
    def is_visible(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(text))
        return self.driver.text