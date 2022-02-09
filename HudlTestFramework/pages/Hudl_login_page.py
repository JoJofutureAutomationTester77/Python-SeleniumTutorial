# Hudl login Page object
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class login_page(BaseDriver):
#    def __init__(self, browser1):
#        super().__init__(browser1)
#        self.browser1 = browser1
# It is possible create also "locator" list to have a clean job

    def insertuser(self):
        self.email = self.browser1.find_element(By.XPATH, "/html/body/div[2]/form[1]/div[2]/div[1]/input")
        self.email.clear()
        self.email.send_keys(self.Read_user())

    def insertpsw(self):
        self.password = self.browser1.find_element(By.XPATH, "//*[@id='password']")
        self.password.click()
        self.password.send_keys(self.Read_psw())

    def insertusercs(self):
            self.email = self.browser1.find_element(By.XPATH, "/html/body/div[2]/form[1]/div[2]/div[1]/input")
            self.email.clear()
            self.email.send_keys(self.Read_usercs())

    def insertpswcs(self):
            self.password = self.browser1.find_element(By.XPATH, "//*[@id='password']")
            self.password.click()
            self.password.send_keys(self.Read_pswcs())

    def access(self):
        Access = self.wait_until_element_is_clickable("/html/body/div[2]/form[1]/div[4]/div/button")
        Access.click()




