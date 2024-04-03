Feature: Test the "Add to cart" functionality

  Background: I am on the Home Page
    Given I am on the Home Page

    @cart
    Scenario: Test that products can be added to shopping cart
      When I enter "nike sb zoom" in the search field
      When I click on the search button
      When I click on the "Add to cart" button
      Then A confirmation message is displayed
      Then Shopping cart displays 1 item
