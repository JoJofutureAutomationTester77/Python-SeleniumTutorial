# All the Precondition scripts
import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    browser1 = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(browser1, 5)
    browser1.get('https://www.hudl.com/')
    browser1.maximize_window()
    loginbtn = browser1.find_element(By.XPATH, "/html/body/div[1]/header/div/a[2]")
    loginbtn.click()
    request.cls.browser1 = browser1
    request.cls.wait = wait
