import time

from appium import webdriver
from pathlib import Path
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# desired_caps = dict(
#
#     deviceName='Android',
#     platformName='Android',
#     app='C:\\Users\\nasim\PycharmProjects\\AppiumTest\\app\Amazon_in.amazon.mShop.android.shopping.apk',
#     appActivity='.activities.PeopleActivity',
# )
desired_caps = {}
desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
# desired_caps['app'] = 'C:\\Users\\nasim\\PycharmProjects\\AppiumTest\\app\\Amazon.apk'
# desired_caps['app'] = str(Path().absolute().parent)+'\\app\\Amazon.apk'
desired_caps['app'] = str(Path().absolute().parent)+'\\app\\Flipboard.apk'
# desired_caps[]


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(10)
#
# # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
# #
# # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
# #
# # wait = WebDriverWait(driver, 10)
# # wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')))
# #
# # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys("Jeans")
# # driver.press_keycode(66)
# # time.sleep(5)
# #
# #
# # # print([my_elem.get_attribute("alt") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//android.widget.EditText[@text='Phone']")))])
# #
# # # for item in product:
# # #     name = item.find_elements(By.XPATH, "//*[contains(@text, 'Amazon Essentials Men's Slim-Fit Stretch Jean')]")
# # #     product_name.append(name)
# # #
# # # print(product_name)

time.sleep(5)
driver.quit()