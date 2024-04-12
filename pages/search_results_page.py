from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "product-box-add-to-cart-button")
    ADD_TO_WISHLIST_BUTTON = (By.CLASS_NAME, "add-to-wishlist-button")

    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "bar-notification.success")

    def are_all_products_displayed(self):
        self.wait_for_element_to_be_present(self.PRODUCT_ITEM, 3)
        product_item_list = self.find_all(self.PRODUCT_ITEM)
        # assert len(product_item_list) > 0
        for item in product_item_list:
            if not item.is_displayed():
                return False

        return True

    def are_all_titles_containing_text(self, text: str):
        titles_list = self.find_all(self.PRODUCT_TITLE)
        # assert len(titles_list) > 0
        for title in titles_list:
            if text.lower() not in title.text.lower():
                return False

        return True

    def click_add_to_cart_button(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_add_to_wishlist_button(self):
        self.click(self.ADD_TO_WISHLIST_BUTTON)

    def is_confirmation_message_displayed(self):
        return self.wait_for_element_to_be_present(self.CONFIRMATION_MESSAGE, 1)
        # return self.find(self.CONFIRMATION_MESSAGE)
