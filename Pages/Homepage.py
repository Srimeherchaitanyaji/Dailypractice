from selenium.webdriver.common.by import By
from DB_connection.DB_Connection import DB
from Pages.Basepage import Basepage
from config.config import TestData


class Homepage(Basepage):
    
    NAVBAR_OPTIONS =  ("//ul[@class = 'nav navbar-nav']/li/a")
    CATEGORY_LIST = ("//h4[@class = 'panel-title']")
    BRAND_LIST = ("//ul[@class = 'nav nav-pills nav-stacked']//li")
    FEATURES_ITEMS_TEXT = ("//div[@class = 'features_items']//div[@class = 'productinfo text-center']//p")
    FEATURES_ITEMS_PRICE = ("//div[@class = 'features_items']//div[@class = 'productinfo text-center']//h2")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def find_navbaroptions(self):
        ls = []
        options = self.findelements(By.XPATH, self.NAVBAR_OPTIONS) 
        for option in options:
            element = option.text.encode('ascii', 'ignore').decode('utf-8').strip()
            ls.append(element)
        return ls
    
    def find_categoryitems(self):
        ls = []
        options = self.findelements(By.XPATH, self.CATEGORY_LIST)
        for i in options:
            element = i.text
            ls.append(element)
        return ls
    
    def find_branditems(self):
        ls = []
        options = self.findelements(By.XPATH, self.BRAND_LIST)
        for i in options:
            element = i.text
            ls.append(element[3:].strip())
        return ls
    
    def items(self):
        ls = []
        options = self.findelements(By.XPATH, self.FEATURES_ITEMS_TEXT)
        for i in options:
            element = i.text
            ls.append((element,))
        return ls.sort()
    
        
    
    
    

