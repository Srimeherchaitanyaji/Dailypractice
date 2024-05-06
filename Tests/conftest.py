from selenium import webdriver
import pytest

from Pages.Registration_and_login_page import Registration_and_Login_Page
from config.config import TestData


@pytest.fixture(scope = 'class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver-mac/chromedriver')
    request.cls.driver = web_driver
    #web_driver.implicitly_wait(10)
    yield
    web_driver.close()