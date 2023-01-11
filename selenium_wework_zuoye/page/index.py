from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wework_zuoye.page.basepage import BasePage
from selenium_wework_zuoye.page.mail_list import Maillist


class Index(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    # def __init__(self):
    #     options=Options()
    #     options.debugger_address='127.0.0.1:9222'
    #     self.driver=webdriver.Chrome(options=options)
    #     self.driver.implicitly_wait(5)
    def goto_mail_list(self):
        self.find(By.ID,'menu_contacts').click()
        # self._driver.find_element(By.ID,'menu_contacts').click()
        return Maillist(self._driver)
