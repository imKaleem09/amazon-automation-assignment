from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_search_galaxy():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    wait = WebDriverWait(driver, 10)

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

    time.sleep(3)
    driver.quit()