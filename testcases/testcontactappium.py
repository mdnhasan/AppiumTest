import time

from appium import webdriver
from pathlib import Path
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from scrollUtility import ScrollUtility

from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select

from appium import webdriver
from pathlib import Path
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from appium.webdriver.common.touch_action import TouchAction



"""Contact App"""

# desired_caps = dict(
#
#     deviceName='Android',
#     platformName='Android',
#     appPackage='com.android.contacts',
#     appActivity='.activities.PeopleActivity',
# )
#
# # appium_service = AppiumService()
# # appium_service.start()
#
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# time.sleep(1)

"""Create New """
# # driver.find_element(By.ID, 'com.android.dialer:id/fab').click()
# # time.sleep(3)
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create new contact").click()
# # driver.find_element(By.ID, 'com.android.contacts:id/floating_action_button_container').click()
# time.sleep(2)
#
# a = driver.find_element(By.ID, "com.android.contacts:id/left_button")
#
# if a.is_displayed():
#     a.click()
#     time.sleep(1)
#
# driver.find_element(By.XPATH, "//android.widget.EditText[@text='First name']").send_keys("Nasim")
# time.sleep(1)
#
# driver.find_element(By.XPATH, "//android.widget.EditText[@text='Last name']").send_keys("Hasan")
# driver.find_element(By.XPATH, "//android.widget.EditText[@text='Phone']").send_keys(random.randint(12, 55))
# driver.hide_keyboard()
# driver.find_element(By.XPATH, "//*[contains(@text, 'SAVE')]").click()
#
# # driver.find_element(By.ID, "com.samsung.android.dialer:id/callButtonContainer").click()
# time.sleep(3)


"""Long Press Section"""
# elements = driver.find_elements(By.ID, 'com.android.contacts:id/cliv_name_textview')
#
# print(len(elements))
#
# actions = TouchAction(driver)
# # actions.tap(elements[1]).perform()
# actions.long_press(elements[1]).perform()
# driver.find_element(By.ID, 'com.android.contacts:id/menu_delete').click()
# time.sleep(2)
# driver.find_element(By.ID,'android:id/button1').click()
#
# time.sleep(3)
#
# driver.quit()

# appium_service.stop()


"""Drag and Drop section with other apk """

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.mobeta.android.demodslv',
    appActivity='.Launcher',
)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(2)

driver.find_element(By.ID, 'com.android.permissioncontroller:id/continue_button').click()
time.sleep(1)
driver.find_element(By.ID, 'android:id/button1').click()
time.sleep(3)

driver.find_elements(By.ID,'com.mobeta.android.demodslv:id/activity_title')[0].click()
time.sleep(2)
elements = driver.find_elements(By.ID, 'com.mobeta.android.demodslv:id/drag_handle')
print(len(elements))

actions = TouchAction(driver)
actions.press(elements[0]).wait(3000).move_to(elements[3]).perform().release()

print("Code Run Successfully")
driver.quit()
