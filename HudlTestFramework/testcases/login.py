#This is a proof to create TestCase as in https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from base.base_driver import BaseDriver

@pytest.mark.usefixtures("setup")
class login_page(BaseDriver):
    def __init__(self):
        super().__init__(self)


    def browsestartpage(self):
        browser1 = webdriver.Chrome(ChromeDriverManager().install())
        self.browser1 = browser1
        browser1.get('https://www.hudl.com/')
        browser1.maximize_window()
        loginbtn = browser1.find_element(By.XPATH, "/html/body/div[1]/header/div/a[2]")
        loginbtn.click()

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

    def LoginSuccess(self):
        link = self.link = self.browser1.find_element(By.XPATH,
                                                      "//*[@id='ssr-webnav']/div/div[1]/nav[2]/div[2]/a/div[2]/span)")
        if link == "MyProjectsample5":
            return ("Test-Passed")
        else:
            pass


if __name__ == '__main__':
    mylogin = login_page(webdriver.Chrome())
    mylogin.insertuser()
    mylogin.insertpsw()
    mylogin.insertusercs()
    mylogin.insertpswcs()
