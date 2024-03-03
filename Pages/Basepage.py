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
        try:
            Text = self.driver.find_element(locator).text
            return Text
        except Exception as E:
            return E
    
    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)
    
    def get_title(self, title):
        try:
            return WebDriverWait(self.driver, 10).until(EC.title_is(title))
        except Exception as E:
            return E
    
    def is_visible(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(text))
        return self.driver.text
    
    def findelement(self, locator):
        try:
            self.driver.find_element(locator)
            return True
        except:
            return False