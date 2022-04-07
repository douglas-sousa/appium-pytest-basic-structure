from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

import config

@pytest.fixture
def driver():
    options = dict(
        platformName='Android',
        platformVersion=config.ANDROID_VERSION,
        automationName='UiAutomator2',
        deviceName=config.EMULATOR_ID,
        app=config.APP_PATH,
        isHeadless=config.IS_HEADLESS,
        avd=config.MOBILE_NAME,
    )
    driver = webdriver.Remote(config.WEBDRIVER_URL, options)
    print("Starting up driver")
    yield driver
    print("Closing down driver")
    driver.quit()

def test_invalid_mail(driver):
    username_input = driver.find_element(By.XPATH, "//*[@text='Username']")
    password_input = driver.find_element(By.XPATH, "//*[@text='Password']")
    login_button = driver.find_element(By.XPATH, "//*[@text='Login']")

    username_input.send_keys('companyx')
    password_input.send_keys('company')
    login_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@text='Invalid username or password!']"))
    )