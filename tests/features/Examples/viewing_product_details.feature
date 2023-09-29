Feature: Viewing Product Details at SauceDemo

  Scenario: View details of a product
    Given I am on the SauceDemo product page
    When I click on the "Sauce Labs Backpack" product name
    Then I should see detailed information about the "Sauce Labs Backpack"

  Scenario: Return to product listing from product details
    Given I am viewing the "Sauce Labs Backpack" product details on SauceDemo
    When I click on the "Back to products" button
    Then I should return to the product listing page
