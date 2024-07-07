from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import pytest





@pytest.fixture(scope = 'class')
def init_driver(request):
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    service = Service(executable_path='../DailyPractice/driver/chromedriver/chromedriver')
    web_driver = webdriver.Chrome(service=service)
    request.cls.driver = web_driver
    #web_driver.implicitly_wait(10)
    yield
    web_driver.close()