from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "Pixel_4a"
options.automationName = "UiAutomator2"
options.appPackage = "org.solovyev.android.calculator"
options.appActivity = ".CalculatorActivity"
#options.set_capability("newCommandTimeout", 300)

print("Starting driver...")
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
wait = WebDriverWait(driver, 10)
print("Driver started. App should open now.")

time.sleep(15)  # wait for app to fully load

#wait.until(EC.element_to_be_clickable((AppiumBy.ID, "org.solovyev.android.calculator:id/wizard_next"))).click()

wait.until(EC.element_to_be_clickable((AppiumBy.ID, "org.solovyev.android.calculator:id/cpp_button_2"))).click()
wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+")'))).click()
wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")'))).click()
wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("=")'))).click()

# Try to get the result text, might need adjustment based on app UI
result = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.TextView"))).text
print("Calculation Result:", result)
time.sleep(5)

# Close the app and quit driver
driver.quit()
print("App closed. Driver quit successfully.")