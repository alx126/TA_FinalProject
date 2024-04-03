from behave import *


# @given('I am on the Home page')
# def step_impl(context):
#     context.home_page.navigate_to_home_page()


@when('I enter "{text}" in the search field')
def step_impl(context, text):
    context.home_page.type_text_in_search_input(text)


@when('I click on the search button')
def step_impl(context):
    context.home_page.click_search_button()


@when('I click on the "Add to cart" button')
def step_impl(context):
    context.search_results_page.click_add_to_cart_button()


@then('A confirmation message is displayed')
def step_impl(context):
    assert context.search_results_page.is_confirmation_message_displayed()


@then('Shopping cart displays {qty} item')
def step_impl(context, qty):
    context.home_page.verify_cart_qty(qty)
