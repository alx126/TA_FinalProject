from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser


class BasePage(Browser):
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")
    CART_QTY = (By.CLASS_NAME, 'cart-qty')
    WISHLIST_QTY = (By.CLASS_NAME, 'wishlist-qty')

    BASE_URL = "https://demo.nopcommerce.com/"

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    def wait_for_text_to_be_present_in_element(self, element_locator, text, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until((EC.text_to_be_present_in_element(element_locator, text)))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_element_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    # va returna True daca expected_url este egal cu URL-ul
    # paginii din care apelam metoda
    def is_url_correct(self, expected_url):
        #return expected_url == self.driver.current_url
        return expected_url in self.driver.current_url

    def type_text_in_search_input(self, text):
        # self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)
        self.type(self.SEARCH_INPUT, text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if not checkbox_element.is_selected():
            self.click(checkbox_element)

    def uncheck_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if checkbox_element.is_selected():
            self.click(checkbox_element)
        #
        # if checkbox_element.is_selected():
        #     self.click(checkbox_element)

    def verify_cart_qty(self, expected):
        expected_qty = f'{expected}'
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.text_to_be_present_in_element(self.CART_QTY, expected_qty))
        self.wait_for_text_to_be_present_in_element(self.CART_QTY, expected_qty, 5)
        assert expected_qty in self.find(self.CART_QTY).text

    def verify_wishlist_qty(self, expected):
        expected_qty = f'{expected}'
        self.wait_for_text_to_be_present_in_element(self.WISHLIST_QTY, expected_qty, 5)
        assert expected_qty in self.find(self.WISHLIST_QTY).text
