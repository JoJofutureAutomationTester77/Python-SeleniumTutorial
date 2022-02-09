import pytest
from base.base_driver import BaseDriver
from pages.HomeHudl import home_hudl
from pages.Hudl_login_page import login_page


@pytest.mark.usefixtures("setup")
class Test_login(BaseDriver):

    def test_login(self):
        # openBrowser and go to login Page
        # Insert Credentials
        lp = login_page(self.browser1)
        lp.insertuser()
        lp.insertpsw()
        lp.access()

        # verify correct login

        hm = home_hudl(self.browser1)
        link = lp.wait_for_home_elements("//*[@id='ssr-webnav']/div/div[1]/nav[2]/div[2]/a/div[2]/span")
        if link == "MyProjectsample5":
            print("Test-Passed")
        else:
            print("Test not Passed")

        hm.logout()
        self.browser1.close()
