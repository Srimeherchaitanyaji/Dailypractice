
import pytest
from Pages.Homepage import Homepage
from Tests.test_basetest import Basetest
from config.config import TestData



@pytest.fixture(scope="class")
def Home_page(request):
    request.cls.homepage = Homepage(request.cls.driver)

@pytest.mark.usefixtures("Home_page")
class Test_homepage(Basetest):

    def test_HP002(self):
        actual_options = self.homepage.find_navbaroptions()
        expected_options = TestData.NAVBAR_OPTIONS
        assert actual_options == expected_options

        


