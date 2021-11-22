from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = int(x_element.text)
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
