import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_zuoye.page.addmember import AddMember
from selenium_wework_zuoye.page.basepage import BasePage


class Maillist(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def goto_add_member(self):
        time.sleep(3)
        # locator=(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # self.wait_for_click(locator)
        # WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator)) #显示等待，元素是不是可以被点击
        def wait_add_member(x):
            element_len= len(self.finds(By.ID, 'username'))
            if element_len<=0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            else:
                return element_len>0
        self.wait_for_elem(wait_add_member)



        # self._driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        # print(ele)
        # ele[1].click()
        return AddMember(self._driver)