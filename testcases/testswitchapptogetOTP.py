import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'net.one97.paytm'
desired_caps['appActivity'] = '.landingpage.activity.AJRMainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'net.one97.paytm:id/et_registered_mobile').click()
driver.press_keycode(16)
driver.press_keycode(14)
driver.press_keycode(8)
driver.press_keycode(8)
driver.press_keycode(8)
driver.press_keycode(8)
driver.press_keycode(8)
driver.press_keycode(12)
driver.press_keycode(12)
driver.press_keycode(15)

driver.hide_keyboard()
# driver.find_element_by_id('net.one97.paytm:id/viewProceedClick').click()
#
# driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
# time.sleep(2)
# driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
#
# driver.find_element_by_xpath("//*[@text='Forgot Password?']").click()
# time.sleep(2)
# driver.find_element_by_id('net.one97.paytm:id/viewProceedClick').click()

driver.start_activity('com.android.mms', '.ui.ConversationList')


# driver.find_elements_by_id('com.android.mms:id/subject')[0].click()
#
messages = driver.find_elements_by_id('com.android.mms:id/text_view')
text = messages[len(messages) - 1].text[83:89]
# print(text[83:89])

time.sleep(5)
driver.quit()