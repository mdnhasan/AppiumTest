import time

import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common import by
from uiautomator import device
from selenium.webdriver.support.select import Select

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='.activities.PeopleActivity',
)

# appium_service = AppiumService()
# appium_service.start()


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(1)

driver.find_element(By.a)

# driver.find_element(By.ID, 'com.android.dialer:id/fab').click()
# time.sleep(3)
driver.find_element(By.ID, 'com.android.contacts:id/floating_action_button').click()
time.sleep(1)

a = driver.find_element(By.ID, "com.android.contacts:id/left_button")

if a.is_displayed():
    a.click()
    time.sleep(1)

driver.find_element(By.XPATH, "//android.widget.EditText[@text='First name']").send_keys("Nasim")
time.sleep(1)

driver.find_element(By.XPATH, "//android.widget.EditText[@text='Last name']").send_keys("Hasan")
driver.find_element(By.XPATH, "//android.widget.EditText[@text='Phone']").send_keys("01673274859")
driver.hide_keyboard()
driver.find_element(By.XPATH, "//*[contains(@text, 'SAVE')]").click()


# driver.find_element(By.ID, "com.samsung.android.dialer:id/callButtonContainer").click()

time.sleep(3)
driver.quit()

# appium_service.stop()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, '')


# driver.find_element(by=appium.accessibility id value='accessibility id')

# driver.find_element(by=appium.accessibility

# driver.find_element(By=AppiumBy.ACCESSIBILITY_ID,value="Button1").click()

driver.find_element(By=AppiumBy.ACCESSIBILITY_ID)