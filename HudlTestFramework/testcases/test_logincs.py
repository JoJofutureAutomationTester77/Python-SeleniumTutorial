# Test Case - Case Sensitive LogIN

import pytest
from base.base_driver import BaseDriver
from pages.Hudl_login_page import login_page


@pytest.mark.usefixtures("setup")
class Test_logincs(BaseDriver):

    def test_login_cs(self):
        # openBrowser and go to login Page (configfiles)
        # Insert Credentials
        lp = login_page(self.browser1)
        lp.insertusercs()
        lp.insertpswcs()
        lp.access()

        # verify that login fails

        self.browser1.close()
