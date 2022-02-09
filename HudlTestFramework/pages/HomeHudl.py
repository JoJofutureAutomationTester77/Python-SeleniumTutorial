# Hudl Main Page

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class home_hudl(BaseDriver):

    def SearchLogout(self):
        browser1 = self.browser1
        self.btn_user = browser1.find_element(By.XPATH,
                                                   "//*[@id='ssr-webnav']/div/div[1]/nav[1]/div[4]/div[2]/div[1]/div[2]/span")
        self.btn_logout = self.browser1.find_element(By.XPATH,
                                                                       "/html/body/div[2]/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a/span")
        self.actionC = ActionChains(self.browser1)



    def logout(self):
        self.actionC.move_to_element(self.btn_user).perform()
        self.btn_logout.click()

    def verifylink(self):
        self.link = self.browser1.find_element(By.XPATH, "//*[@id='ssr-webnav']/div/div[1]/nav[2]/div[2]/a/div[2]/span)")
