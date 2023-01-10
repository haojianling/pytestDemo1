import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click=self.driver.find_element(By.XPATH,"//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action=ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        time.sleep(3)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_move_toelement(self):
        self.driver.get("https://www.baidu.com")
        ele=self.driver.find_element(By.CSS_SELECTOR,"#s-usersetting-top")
        action=ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    def test_dragdrog(self):#拖拽一个元素到另外一个元素上
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag=self.driver.find_element(By.ID,'dragger')
        ele_drog=self.driver.find_element(By.XPATH,'/html/body/div[2]')
        action=ActionChains(self.driver)
        # action.drag_and_drop(ele_drag,ele_drog)  #方式一
        #action.click_and_hold(ele_drag).release(ele_drog) #方式二
        action.click_and_hold(ele_drag).move_to_element(ele_drog).release() #方式三
        action.perform()
        time.sleep(3)

    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele1=self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        ele2= self.driver.find_element(By.XPATH, '/html/body/label[2]/table/tbody/tr/td[2]/input')
        ele1.click()
        action=ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-v', '-s','test_ActionChains.py'])