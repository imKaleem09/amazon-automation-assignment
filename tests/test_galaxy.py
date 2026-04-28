from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# LambdaTest credentials
username = "kaleem897998"
access_key = "LT_MKOSJBtfno0BU6r5phe51h46Tz8QbIKzqru6dOGFcaPBEQ3"

grid_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

def test_search_galaxy():
    options = Options()

    lt_options = {
        "platformName": "Windows 10",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "build": "Amazon Automation Build",
        "name": "Galaxy Test"
    }

    options.set_capability("LT:Options", lt_options)

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )

    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    box.send_keys("Samsung Galaxy S24")
    box.send_keys(Keys.ENTER)

    product = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]"))
    )
    product.click()

    tabs = driver.window_handles
    if len(tabs) > 1:
        driver.switch_to.window(tabs[1])

    try:
        price = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
        ).text
        print("Price is:", price)
    except:
        print("Price not found")

    try:
        cart = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='add-to-cart-button']"))
        )
        cart.click()
        print("Added to cart")
    except:
        print("Cart button not found")

    time.sleep(5)
    driver.quit()