import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize('id_lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905",])
def test_reply_sending(driver, id_lesson):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{id_lesson}/step/1"
    driver.implicitly_wait(25)
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, ('[placeholder="Напишите ваш ответ здесь..."]')).send_keys(str(answer))
    driver.find_element(By.CSS_SELECTOR, ('.submit-submission')).click()
    text = driver.find_element(By.CSS_SELECTOR, ('.smart-hints__hint')).text
    if text != "Correct!":
        print(text)
