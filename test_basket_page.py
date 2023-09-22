from .pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open() # Гость открывает главную страницу
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке сайта
    page.is_not_product_in_basket() # Ожидаем, что в корзине нет товаров
    page.is_basket_empty_text() # Ожидаем, что есть текст о том что корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = BasketPage(browser, link)
    page.open() # Гость открывает страницу товара
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке
    page.is_not_product_in_basket() # Ожидаем, что в корзине нет товаров
    page.is_basket_empty_text() # Ожидаем, что есть текст о том что корзина пуста