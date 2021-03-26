from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_css_selector("#num1").text)
    y = int(browser.find_element_by_css_selector("#num2").text)
    q = str(x + y)
    browser.find_element_by_css_selector("#dropdown").click()
    browser.find_element_by_css_selector("[value='" + q + "']").click()

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
