from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.implicitly_wait(12)
    driver.get(link)

    text = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    driver.find_element(By.CSS_SELECTOR, ('#book')).click()

    button = driver.find_element(By.CSS_SELECTOR, ('#solve'))
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    x = int(driver.find_element_by_css_selector("#input_value").text)
    driver.find_element_by_css_selector("#answer").send_keys(calc(x))
    button.click()

finally:
    time.sleep(5)
    driver.quit()