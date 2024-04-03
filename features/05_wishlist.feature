Feature: Test the Wishlist functionality

    Background: I am on the Home Page
    Given I am on the Home Page

      @wish
      Scenario: Test that the user can add products to wishlist
        When I enter "nike sb zoom" in the search field
        When I click on the search button
        When I click on the "Add to wishlist" button
        Then A confirmation message is displayed
        Then Wishlist displays 1 item