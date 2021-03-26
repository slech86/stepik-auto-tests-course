from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("[name='firstname']").send_keys('firstname')
    browser.find_element_by_css_selector("[name='lastname']").send_keys('lastname')
    browser.find_element_by_css_selector("[name='email']").send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson2_step8.txt')

    browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
