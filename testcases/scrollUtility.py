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


class ScrollUtility:
    @staticmethod
    def ScrolltoText(text, driver):
        try:
            # c = driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')
            e = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                    "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView("
                                    "new UiSelector().textContains(\"" + text + "\").instance(0))")
            e.click()

        except NoSuchElementException:
            print("Scrollable Not found")

    # @staticmethod
    # def swipeUp(howMany, driver):
    #     for i in range(1, 4):
    #         driver.swipe(514, 600, 514, 200, 1000)
    #
    # @staticmethod
    # def swipeDown(howMany, driver):
    #     for i in range(1, 4):
    #         driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)