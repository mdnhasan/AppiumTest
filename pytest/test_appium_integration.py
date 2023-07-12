import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
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
# from scrollUtility import ScrollUtility

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


"""FOr Failed Test Case Take Screenshot"""


# @pytest.fixture() ###Commented when use global varialbe from conftest file
# def log_on_failure(request,appium_driver):
#     yield
#     item = request.node
#     driver =appium_driver
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="Screenshot",
#                       attachment_type=AttachmentType.PNG)  ###Success Sceenshot


def getData():
    return [

        ['Delhi'],
        ['Dubai'],

    ]


"""Lesson learn 'Never use name change'"""

"""setup (For run once in one test case if two value like dubai and delhi)"""
"""setup_function (For run times need in one test case if two or more value like dubai and delhi)"""


# def setup_function():  ###Commented when use global varialbe from conftest file
#     global driver
#     desired_caps = {}
#     desired_caps['deviceName'] = 'Android'
#     desired_caps['platformName'] = 'Android'
#     desired_caps['appPackage'] = 'com.goibibo'
#     desired_caps['appActivity'] = '.common.HomeActivity'
#     desired_caps['noReset'] = True
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     driver.implicitly_wait(5)
#
#
# def teardown_function():
#     time.sleep(3)
#     driver.quit()

###########################################################################
# # @pytest.mark.usefixtures("log_on_failure")
# @pytest.mark.parametrize("city", getData())
# def test_login(city,appium_driver):
#     driver = appium_driver
#     driver.find_element(By.XPATH, "//android.widget.TextView[@text='Hotels']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//android.widget.TextView[@text='City, Area or Property Name']").click()
#     time.sleep(2)
#     print(city)
#     driver.find_element(By.ID, "com.goibibo:id/edtSearch").send_keys(city)
#     time.sleep(2)
#     driver.find_elements(By.ID, "com.goibibo:id/lytChildNode1")[0].click()
#     time.sleep(4)
#     driver.find_element(By.ID, "com.goibibo:id/verticalHomeSearchButton").click()
#     time.sleep(10)
#     citytext = driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Top Areas to Stay')]").text
#     print(citytext)
#     """Attach Screenshot to allure report"""
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG) ###Success Sceenshot

########################################################################################

# driver.swipe(1130,834,0,0,1000) nto scroll any place with point location

#####################

def test_searchVillas(appium_driver):
    driver = appium_driver
    time.sleep(10)
    driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text='Cabs')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='City, Area or Landmark']").click()
    time.sleep(2)
    driver.find_element(By.ID, "com.goibibo:id/edtSearch").send_keys("Delhi")
    time.sleep(2)
    driver.find_elements(By.ID, "com.goibibo:id/lytChildNode1")[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='Other']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='14']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text='Continue')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//android.widget.Button[@text='Search Hourly Stays']").click()
    time.sleep(5)
    elem= driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new '
                                 'UiSelector().textContains("Hotel The Ventus by Hotel vegas").instance(0))')
    elem.click()
    time.sleep(5)






#######Code From Lecture##############
#
# import time
#
# import pytest
# from appium import webdriver
# from appium.webdriver.appium_service import AppiumService
#
# def get_data():
#     return [
#
#         ["Delhi"],
#         ["Dubai"],
#
#     ]
#
# def setup_function():
#     global appium_service
#     appium_service = AppiumService()
#     appium_service.start()
#
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['deviceName'] = 'Android'
#     desired_caps['appPackage'] = 'com.goibibo'
#     desired_caps['appActivity'] = '.common.HomeActivity'
#     desired_caps['noReset'] = True
#     global driver
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     driver.implicitly_wait(10)
#
# def teardown_function():
#     time.sleep(2)
#     driver.quit()
#     appium_service.stop()
#
# @pytest.mark.parametrize("city", get_data())
# def test_dologin(city):
#     driver.find_element_by_id('com.goibibo:id/btn1').click()
#     driver.find_element_by_accessibility_id('destination').click()
#     driver.find_element_by_id('com.goibibo:id/edtSearch').send_keys(city)
#     driver.find_elements_by_id('com.goibibo:id/lytLocationItem')[0].click()
#     driver.find_element_by_xpath("//android.widget.TextView[@text='Search']").click()
#     cityText = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'EXPLORE')]").text
#     print(cityText)
#     newCityText = str(cityText).replace("EXPLORE ", "").replace("!", "")
#     print(newCityText)
#
#     assert newCityText in str(city).upper()
