import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='12.0'
# desired_caps['deviceName']='vivo iQOO Neo3'
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# driver.quit()

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'
desired_caps['deviceName']='vivo iQOO Neo3'
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='.view.WelcomeActivityAlias'
# desired_caps['appActivity']='.mainnesting.view.MainVisitorActivity'
desired_caps['noReset']="true"
desired_caps['dontStopAppOnReset']='true'
desired_caps['skipDeviceInitialization']='true'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
el1 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_dis_agree")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView[2]")
el2.click()
time.sleep(3)
driver.back()
driver.quit()