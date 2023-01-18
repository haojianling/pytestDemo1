from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desire_cap={
"platformName": "Android",
"appium:platformVersion": "6.0.1",
"appium:deviceName": "vivo_iQOO_Neo3",
"appium:appPackage": "com.xueqiu.android",
"appium:appActivity": ".view.WelcomeActivityAlias",
    "noReset":True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
driver.implicitly_wait(10)
el3 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
el3.click()
el3.send_keys("alibaba")
el4 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView")
el4.click()
