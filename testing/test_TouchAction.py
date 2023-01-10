import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


class TestTouchAction():
    def setup(self):
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('w3c',False)
        # self.driver=webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        el=self.driver.find_element(By.ID,'kw')
        el.send_keys('selenium测试')
        el_search=self.driver.find_element(By.ID, 'su')
        el_search.click()
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(5)


