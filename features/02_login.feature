Feature: Test the functionality of the Login Page


  Background: I am on the Login Page
    Given I am on the Login Page


  @simple @login @url
  Scenario: Check that the url is correct
    Then Login page URL is "https://demo.nopcommerce.com/login"


  @login @success
    #Se ruleaza dupa "Test complete registration"
  Scenario: Check that the login is done successfully with a registered account
    When I insert "alex.popa@fakes.com" in the email input
    When I insert "myPassw0rd" in the password input
    When I click on the login button
    Then Login page URL is "https://demo.nopcommerce.com/"
    Then "My account" button is displayed
    Then "Log out" button is displayed
    Then "Wishlist" button is displayed
    Then "Shopping cart" button is displayed
    Then "Log out" button is displayed on top

  @simple @smoke @login
  #Scenariu fara parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an
    unregistered email
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found" message

  @parameterized @smoke @login
  #Scenariu cu parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an
    unregistered email
    When I insert "wrong_email@host.com" in the email input
    When I insert "parolaoarecare" in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found"

  @parameterized @regression @login
  Scenario: Check that "Please enter your email" message is displayed when the user enters empty email address
    When I insert " " in the email input
    When I click on the login button
    Then Email error message is displayed
    Then Email error message text is "Please enter your email"

  @parameterized @regression @login
  Scenario: Check that "Wrong email" message is displayed when the user enters an email address with an invalid format
    When I insert "emailinvalid" in the email input
    When I click on the login button
    Then Email error message is displayed
    Then Email error message text is "Wrong email"


