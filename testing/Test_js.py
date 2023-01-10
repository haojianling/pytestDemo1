import time

from selenium.webdriver.common.by import By

from testing.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys('selenium测试')
        element=self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='page']/div/a[10]").click()
        time.sleep(3)
        # for code in['return document.title','return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element=self.driver.execute_script("return document.getElementById('train_date')")
        self.driver.execute_script("document.getElementById('train_date').value='2023-1-10'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
