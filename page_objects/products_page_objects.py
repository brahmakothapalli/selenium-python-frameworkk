from base.BasePage import BasePage
from utils import logger_config
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPageObjects(BasePage):
    logger = logger_config.get_logger()

    # locators
    __products_text = (By.XPATH, "//div[@class='header_secondary_container']/span")
    __cart_icon = (By.XPATH, "//div[@id='shopping_cart_container']/a")
    __sauce_lab_backpack_add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def is_products_page_displayed(self) -> bool:
        return self.find(self.__products_text).is_displayed()

    def get_products_page_text(self) -> str:
        return self.get_text(self.__products_text)

    def is_cart_icon_displayed(self) -> None:
        assert self.find(self.__cart_icon).is_displayed()

    def add_backpack_to_cart(self) -> None:
        self.click(self.__sauce_lab_backpack_add_to_cart)

    def navigate_to_cart(self) -> None:
        self.click(self.__cart_icon)
