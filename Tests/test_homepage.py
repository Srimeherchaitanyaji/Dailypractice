
import pytest
from Pages.Homepage import Homepage
from Tests.test_basetest import Basetest
from DB_connection.DB_Connection import DB
from config.config import TestData



@pytest.fixture(scope="class")
def Home_page(request):
    request.cls.homepage = Homepage(request.cls.driver)
    request.cls.database = DB()

@pytest.mark.usefixtures("Home_page")
class Test_homepage(Basetest):

    def test_HP002(self):
        actual_options = self.homepage.find_navbaroptions()
        expected_options = TestData.NAVBAR_OPTIONS
        assert actual_options == expected_options

    def test_HP003(self):
        actual_options = self.homepage.find_categoryitems()
        expected_options = TestData.CATEGORY_OPTIONS
        assert actual_options == expected_options

    def test_HP004(self):
        actual_options = self.homepage.find_branditems()
        expected_options = TestData.BRAND_ITEMS
        assert actual_options == expected_options

    def test_HP005(self):
        expected_items = self.database.select_items()
        actual_items = self.homepage.items()
        assert actual_items == expected_items
        
    def test_HP006(self):
        expected_output = self.database.items_and_prices()
        actual_output = self.homepage.check_items_and_prices()
        assert actual_output == expected_output




        


