from page_objects.login_page_objects import LoginPageObjects
from page_objects.products_page_objects import ProductPageObjects
from utils.read_configuration import ReadConfiguration


class TestProductPage:
    url = ReadConfiguration.get_url()
    user_name = ReadConfiguration.get_username()
    password = ReadConfiguration.get_password()

    def test_add_item_to_cart(self, get_driver):
        driver = get_driver
        login_page = LoginPageObjects(driver)
        login_page.enter_user_credentials(self.user_name, self.password)
        login_page.click_login_button()
        product_page = ProductPageObjects(driver)
        assert product_page.get_product_page_title() == "PRODUCTS"
        product_page.add_backpack_to_cart()
        if product_page.get_cart_item_count() == 1:
            print("Product added successfully to the car")
        else:
            print("Failed to add the product to the cart")
