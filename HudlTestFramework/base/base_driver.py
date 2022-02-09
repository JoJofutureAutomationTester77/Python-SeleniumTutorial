# All commands, methods class that we can use in all tests to simplify the scripts
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located


class BaseDriver():
    def __init__(self, browser1):
        self.browser1 = browser1

    def wait_for_home_elements(self, locator_type, locator):
        wait = WebDriverWait(self.browser1, 5)
        home_element = wait.until(presence_of_element_located(locator_type))

        return home_element

    def wait_until_element_is_clickable(self, locator_type):
        wait = WebDriverWait(self.browser1, 5)
        element = wait.until(element_to_be_clickable(locator_type))
        return element

    def Read_user(self):
        read = open('.\testdata\Credential', 'r')
        line = read.readlines()
        user = line[0]
        return user

    def Read_psw(self):
        read = open('.\testdata\Credentials', 'r')
        line = read.readlines()
        password = line[1]
        return password

    def Read_usercs(self):
        read = open('.\testdata\Credential', 'r')
        line = read.readlines()
        user = line[2]
        return user

    def Read_pswcs(self):
        read = open('./Credentials', 'r')
        line = read.readlines()
        password = line[3]
        return password
