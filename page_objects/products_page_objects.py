from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ProductPageObjects:
    product_page_title = (By.XPATH, "//span[text()='Products']")
    backpack_add_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    shopping_cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        self.driver = driver

    def get_product_page_title(self):
        return self.driver.find_element(*self.product_page_title).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_cart_button).click()

    def get_cart_item_count(self):
        try:
            return int(self.driver.find_element(*self.shopping_cart_badge).text)
        except NoSuchElementException:
            return 0

