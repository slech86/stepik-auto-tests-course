import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_checking_if_there_is_a_button_to_add_a_product_to_the_cart(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR,('#id_quantity + .btn'))
    assert len(button) > 0, 'Кнопка добавления товара в корзину отсутсвует'

# Так как селектор на кнопку уникальный, использую "elements", а не "element" и если кнопка есть на сайте,
# assert-ом проверяю на наличие хотя бы одного элеметна в "button". Таким образом тест не упадет до проверки assert-ом
# при отсутствии кнопки для добавления товара в корзину