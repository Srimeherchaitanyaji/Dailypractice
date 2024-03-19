from selenium.webdriver.common.by import By
from Pages.Basepage import Basepage
from config.config import TestData


class Homepage(Basepage):
    
    NAVBAR_OPTIONS =  "//ul[@class = 'nav navbar-nav']/li/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def find_navbaroptions(self):
        ls = []
        options = self.findelements(By.XPATH,self.NAVBAR_OPTIONS) 
        for option in options:
            element = option.text.encode('ascii', 'ignore').decode('utf-8').strip()
            ls.append(element)
        return ls
