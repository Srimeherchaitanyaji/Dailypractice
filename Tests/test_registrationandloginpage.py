import pytest
from Pages.Registration_and_login_page import Registration_and_Login_Page
from Tests.test_basetest import Basetest
from config.config import TestData


@pytest.fixture(scope="class")
def registration_and_login_page(request):
    request.cls.R_L_page = Registration_and_Login_Page(request.cls.driver)


@pytest.mark.usefixtures("registration_and_login_page")
class Test_registration_and_login_page(Basetest):


    def test_RL002(self):
        self.R_L_page.do_click(self.R_L_page.LOGIN_SIGNUP_PAGE_OPTION)
        assert self.R_L_page.get_pagetitle()
        
        

    def test_RL003(self):
        actual_heading = self.R_L_page.get_headings(self.R_L_page.SIGNIN_TITLE)
        expected_heading = TestData.LOGIN_HEADING
        assert actual_heading == expected_heading
        

    def test_RL004(self):
        assert self.R_L_page.find_loginfields

    def test_RL005(self):
        assert self.R_L_page.login_placeholders

    def test_RL006(self):
        assert self.R_L_page.find_login_button

    def test_RL007(self):
        actual_heading = self.R_L_page.get_headings(self.R_L_page.SIGNUP_TITLE)
        expected_heading = TestData.SIGNUP_HEADING
        assert actual_heading == expected_heading

    def test_RL008(self):
        assert self.R_L_page.find_signupfields

    def test_RL009(self):
        assert self.R_L_page.signup_placeholders

    def test_RL010(self):
        assert self.R_L_page.find_signup_button

    def test_RL011(self):
        assert self.R_L_page.find_logo

    def test_RL012(self):
        assert self.R_L_page.find_OR_text

    def test_RL013(self):
        assert self.R_L_page.find_subscription_text

    def test_RL014(self):
        assert self.R_L_page.find_subscription_emailfield

    def test_RL015(self):
        assert self.R_L_page.find_subscription_placeholder
    
    def test_RL016(self):
        assert self.R_L_page.find_subscribe_button

    def test_RL018(self):
        self.R_L_page.do_login(TestData.LOGIN_EMAIL,TestData.PASSWORD)
        Actual_msg =  self.R_L_page.find_errormessage()
        Expected_msg = TestData.ERROR_MESSAGE
        assert Actual_msg == Expected_msg

    def test_RL021(self):
        self.R_L_page.do_signup(TestData.USERNAME,TestData.SIGNUP_EMAIL)
        Actual_msg = self.R_L_page.find_signup_errormessage()
        Expected_msg = TestData.SIGNUP_ERRORMESSAGE
        assert Actual_msg == Expected_msg

        

    




        

        







        


        
        



        
        
        


