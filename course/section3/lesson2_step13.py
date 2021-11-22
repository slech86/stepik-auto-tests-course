from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver = webdriver.Chrome()
        driver.get(link)

        # Ваш код, который заполняет обязательные поля
        driver.find_element_by_css_selector(".first_block .first").send_keys("input_1")
        driver.find_element_by_css_selector(".first_block .second").send_keys("input_2")
        driver.find_element_by_css_selector(".third").send_keys("input_3")

        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Описание ошибки")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        driver.get(link)

        # Ваш код, который заполняет обязательные поля
        driver.find_element_by_css_selector(".first_block .first").send_keys("input_1")
        driver.find_element_by_css_selector(".first_block .second").send_keys("input_2")
        driver.find_element_by_css_selector(".third").send_keys("input_3")

        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Описание ошибки")


if __name__ == "__main__":
    unittest.main()
