from selenium import webdriver
import pytest


@pytest.fixture
def init_driver(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    #web_driver.implicitly_wait(10)
    yield
    web_driver.close()