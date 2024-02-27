
from Pages.Registration_and_login_page import Registration_and_Login_Page
from Tests.test_basetest import Basetest


class Test_registration_and_login_page(Basetest):

    def test_RP002(self):
        self.R_L_page = Registration_and_Login_Page(self.driver)
        self.R_L_page.do_click(self.R_L_page.LOGIN_SIGNUP_PAGE_OPTION)
        signin_title = self.R_L_page.get_headings(self.R_L_page.SIGIN_TITLE)
        assert signin_title
        signup_title = self.R_L_page.get_headings(self.R_L_page.SIGNUP_TITLE)
        assert signup_title
        


