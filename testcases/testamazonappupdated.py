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
from testcases.scrollUtility import ScrollUtility

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.amazon.mShop.android.shopping',
    appActivity='com.amazon.mShop.splashscreen.StartupActivity'
)
# desired_caps = {}
# desired_caps['deviceName'] = 'Android'
# desired_caps['platformName'] = 'Android'
# desired_caps['appPackage'] = 'com.amazon.mShop.android.shopping'
# desired_caps['appActivity'] = 'com.amazon.mShop.splashscreen.StartupActivity'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

try:
    a = driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_deny_button")
    if a.is_displayed():
        a.click()
        time.sleep(2)
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Done']")))
        # driver.find_element(By.XPATH, "//android.widget.Button[@text='Done']").click()
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')))
        # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()

except NoSuchElementException:
    print("Permission page not found")

try:
    b = driver.find_element(By.XPATH, "//android.widget.Button[@text='Done']")

    if b.is_displayed():
        b.click()
        time.sleep(2)
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')))
        # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
        # time.sleep(1)

except NoSuchElementException:
    print("Language Page Not Found")

try:
    # c = driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')
    d = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip sign in")')
    if d.is_displayed():
        d.click()

except NoSuchElementException:
    print("Skip Sign not found")

time.sleep(15)

driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
time.sleep(5)

wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')))

driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys("Jeans")
# time.sleep(4)
driver.press_keycode(0x00000042)
time.sleep(5)

# ScrollUtility.ScrolltoText("Lee Men", driver)  ### import from scrollutility class
# try:
#     # c = driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')
#     e = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#                             'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Lee Men").instance(0))')
#     e.click()
#
# except NoSuchElementException:
#     print("Scrollable Not found")
#
# time.sleep(2)

# driver.swipe(550, 600, 550, 200, 1000) ### Auto Scroll down code
# driver.swipe(550, 600, 550, 200, 1000)
# driver.swipe(550, 600, 550, 200, 1000)

print("Code Run Successfully")
driver.quit()
