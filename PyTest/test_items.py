import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button_present(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(5)  # Для визуальной проверки локализации
    # Проверяем, что кнопка добавления в корзину существует
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена на странице!"
