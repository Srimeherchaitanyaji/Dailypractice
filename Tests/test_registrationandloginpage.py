
from Pages.Registration_and_login_page import Registration_and_Login_Page
from Tests.test_basetest import Basetest
from config.config import TestData


class Test_registration_and_login_page(Basetest):

    def test_RL002(self):
        self.R_L_page = Registration_and_Login_Page(self.driver)
        self.R_L_page.do_click(self.R_L_page.LOGIN_SIGNUP_PAGE_OPTION)
        assert self.R_L_page.get_pagetitle()
        
        

    def test_RL003(self):
        self.R_L_page = Registration_and_Login_Page(self.driver)
        self.R_L_page.do_click(self.R_L_page.LOGIN_SIGNUP_PAGE_OPTION)
        signin_title = self.R_L_page.get_headings(self.R_L_page.SIGIN_TITLE)
        assert signin_title

    def test_RL004(self):
        self.R_L_page = Registration_and_Login_Page(self.driver)
        self.R_L_page.do_click(self.R_L_page.LOGIN_SIGNUP_PAGE_OPTION)
        assert self.R_L_page.find_loginfields

    def test_RL005(self):
        self.R_L_page = Registration_and_Login_Page(self.driver)
        self.R_L_page.do_click(self.R_L_page.LOGIN_SIGNUP_PAGE_OPTION)
        assert self.R_L_page.login_placeholders
        



        
        
        


