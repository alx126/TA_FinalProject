from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):

    MALE_RADIO_BUTTON = (By.ID, "gender-male")
    FEMALE_RADIO_BUTTON = (By.ID, "gender-female")
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    DAY_DROPDOWN = (By.NAME, "DateOfBirthDay")
    MONTH_DROPDOWN = (By.NAME, "DateOfBirthMonth")
    YEAR_DROPDOWN = (By.NAME, "DateOfBirthYear")
    EMAIL_INPUT = (By.ID, "Email")
    COMPANY_INPUT = (By.ID, "Company")
    NEWSLETTER_CHECKBOX = (By.ID, "Newsletter")
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    FIRST_NAME_ERROR = (By.ID, "FirstName-error")
    LAST_NAME_ERROR = (By.ID, "LastName-error")
    EMAIL_ERROR = (By.ID, "Email-error")
    PASSWORD_ERROR = (By.ID, "Password-error")
    CONFIRM_PASSWORD_ERROR = (By.ID, "ConfirmPassword-error")
    WRONG_EMAIL_ERROR = (By.XPATH, "//*[@class='message-error validation-summary-errors']/ul/li") #CLASS_NAME, "message-error"
    ALREADY_REGISTERED_EMAIL_ERROR = (By.CLASS_NAME, "message-error")
    ALREADY_REGISTERED_EMAIL_ERR_MSG = (By.XPATH, "//*[@class='message-error validation-summary-errors']/ul/li")

    COMPLETE_REGISTRATION_MESSAGE = (By.CLASS_NAME, 'result')

    REGISTER_PAGE_URL = "https://demo.nopcommerce.com/register"
    # https://demo.nopcommerce.com/registerresult/1

    def navigate_to_register_page(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    def select_male_radio_button(self):
        self.click(self.MALE_RADIO_BUTTON)

    def select_female_radio_button(self):
        self.click(self.FEMALE_RADIO_BUTTON)

    def set_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def select_date_of_birth_day(self, day):
        self.select_dropdown_option_by_text(self.DAY_DROPDOWN, day)

    def select_date_of_birth_month(self, month):
        self.select_dropdown_option_by_text(self.MONTH_DROPDOWN, month)

    def select_date_of_birth_year(self, year):
        self.select_dropdown_option_by_text(self.YEAR_DROPDOWN, year)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_company_name(self, company_name):
        self.type(self.COMPANY_INPUT, company_name)

    def check_newsletter_checkbox(self):
        self.check_checkbox(self.NEWSLETTER_CHECKBOX)

    def uncheck_newsletter_checkbox(self):
        self.uncheck_checkbox(self.NEWSLETTER_CHECKBOX)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def set_confirm_password(self, password):
        self.type(self.CONFIRM_PASSWORD_INPUT, password)

    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def is_first_name_error_displayed(self):
        assert self.is_element_displayed(self.FIRST_NAME_ERROR)

    def is_last_name_error_displayed(self):
        assert self.is_element_displayed(self.LAST_NAME_ERROR)

    def is_email_error_displayed(self):
        assert self.is_element_displayed(self.EMAIL_ERROR)

    def get_register_email_error_text(self):
        return self.get_element_text(self.EMAIL_ERROR)

    def get_register_wrong_email_error_text(self):
        assert self.get_element_text(self.WRONG_EMAIL_ERROR)

    def is_wrong_email_error_displayed(self):
        assert self.is_element_displayed(self.WRONG_EMAIL_ERROR)

    def is_password_error_displayed(self):
        assert self.is_element_displayed(self.PASSWORD_ERROR)

    def is_password_confirm_error_displayed(self):
        assert self.is_element_displayed(self.CONFIRM_PASSWORD_ERROR)

    def is_complete_registration_message_displayed(self):
        assert self.is_element_displayed(self.COMPLETE_REGISTRATION_MESSAGE)

    def is_already_registered_email_message_displayed(self):
        return self.is_element_displayed(self.ALREADY_REGISTERED_EMAIL_ERROR)

    def get_already_registered_email_message_text(self):
        return self.get_element_text(self.ALREADY_REGISTERED_EMAIL_ERR_MSG)

