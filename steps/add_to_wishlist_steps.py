from behave import *


@when('I click on the "Add to wishlist" button')
def step_impl(context):
    context.search_results_page.click_add_to_wishlist_button()


@then('Wishlist displays {qty} item')
def step_impl(context, qty):
    context.home_page.verify_wishlist_qty(qty)
