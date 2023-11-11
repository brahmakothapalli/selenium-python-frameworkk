from page_objects.login_page_objects import LoginPageObjects


class TestProductsPageScenarios:

    def test_add_product_to_cart(self, get_driver):
        login_page = LoginPageObjects(get_driver)
        login_page.enter_user_credentials("standard_user", "secret_sauce")
        products_page = login_page.click_login_button()
        products_page.add_backpack_to_cart()
        products_page.navigate_to_cart()
