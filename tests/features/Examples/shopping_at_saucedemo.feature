Feature: Shopping at SauceDemo

  Scenario: Add an item to the cart
    Given I am on the SauceDemo product page
    When I click on the "Add to cart" button for "Sauce Labs Backpack"
    Then "Sauce Labs Backpack" should be added to my cart

  Scenario: Remove an item from the cart
    Given I have "Sauce Labs Backpack" in my cart
    When I click on the "Remove" button for "Sauce Labs Backpack"
    Then "Sauce Labs Backpack" should be removed from my cart

  Scenario: Checkout with items in the cart
    Given I have items in my cart
    When I click on the checkout button
    And I complete the checkout process
    Then I should see a confirmation message
