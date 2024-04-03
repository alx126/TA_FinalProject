from behave import *


@given('I am on the Register Page')
def step_impl(context):
    context.register_page.navigate_to_register_page()


@when('I select male gender')
def step_impl(context):
    context.register_page.select_male_radio_button()


@when('I insert "{first_name}" in the First name field')
def step_impl(context, first_name):
    context.register_page.set_first_name(first_name)


@when('I insert "{last_name}" in the Last name field')
def step_impl(context, last_name):
    context.register_page.set_last_name(last_name)


@when('I select day "{day}" for Date of birth')
def step_impl(context, day):
    context.register_page.select_date_of_birth_day(day)


@when('I select month "{month}" for Date of birth')
def step_impl(context, month):
    context.register_page.select_date_of_birth_month(month)


@when('I select year "{year}" for Date of birth')
def step_impl(context, year):
    context.register_page.select_date_of_birth_year(year)


@when('I insert "{email}" in the Email field')
def step_impl(context, email):
    context.register_page.set_email(email)


@when('I insert "{company_name}" in the Company name field')
def step_impl(context, company_name):
    context.register_page.set_company_name(company_name)


@when('I check the Newsletter checkbox')
def step_impl(context):
    context.register_page.check_newsletter_checkbox()


@when('I uncheck the Newsletter checkbox')
def step_impl(context):
    context.register_page.uncheck_newsletter_checkbox()


@when('I insert "{password}" in the Password field')
def step_impl(context, password):
    context.register_page.set_password(password)


@when('I insert "{password}" in the Confirm password field')
def step_impl(context, password):
    context.register_page.set_confirm_password(password)


@when('I click on the Register button')
def step_impl(context):
    context.register_page.click_register_button()


@then('First name error is displayed')
def step_impl(context):
    assert context.register_page.is_first_name_error_displayed()


@then('Last name error is displayed')
def step_impl(context):
    assert context.register_page.is_last_name_error_displayed()


@then('Email error is displayed')
def step_impl(context):
    assert context.register_page.is_email_error_displayed()


@then('Wrong email error is displayed')
def step_impl(context):
    assert context.register_page.is_wrong_email_error_displayed()


@then('Email error text is "{message}"')
def step_impl(context, message):
    assert context.register_page.get_register_email_error_text() == message


@then('Wrong email error text is "{message}"')
def step_impl(context, message):
    assert context.register_page.get_register_wrong_email_error_text() == message


@then('Password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()


@then('Confirm password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_confirm_error_displayed()


@then('Completed registration message is displayed')
def step_impl(context):
    assert context.register_page.is_complete_registration_message_displayed()


@then('"{message}" message is displayed')
def step_impl(context, message):
    assert context.register_page.get_already_registered_email_message_text() == message

