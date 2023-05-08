Feature: Test the functionality of the Register Page

    Background: I am on the Register Page
    Given I am on the Register Page

    @simple
    Scenario: Check that trying to register without completing any field displays error fields
      When I click on the Register button
      Then First name error is displayed
      Then Last name error is displayed
      Then Email error is displayed
      Then Password error is displayed
      Then Confirm password error is displayed

      @register
      Scenario: Test complete registration
        When I select male gender
        When I insert "Alex" in the First name field
        When I insert "Popa" in the Last name field
        When I select day "26" for Date of birth
        When I select month "May" for Date of birth
        When I select year "2015" for Date of birth
        When I insert "alex.popa@fake.com" in the Email field
        When I insert "APOLLO SRL" in the Company name field
        When I check the Newsletter checkbox
        When I insert "myPassw0rd" in the Password field
        When I insert "myPassw0rd" in the Confirm password field
        When I click on the Register button
        Then Completed registration message is displayed


        # https://demo.nopcommerce.com/registerresult/1?returnUrl=/
