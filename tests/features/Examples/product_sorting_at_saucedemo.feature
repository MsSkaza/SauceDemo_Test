Feature: Product Sorting at SauceDemo

  Scenario: Sort products by price (low to high)
    Given I am on the SauceDemo product page
    When I select "Price (low to high)" from the sorting dropdown
    Then the products should be sorted by price in ascending order

  Scenario: Sort products by price (high to low)
    Given I am on the SauceDemo product page
    When I select "Price (high to low)" from the sorting dropdown
    Then the products should be sorted by price in descending order

  Scenario: Sort products by name (A to Z)
    Given I am on the SauceDemo product page
    When I select "Name (A to Z)" from the sorting dropdown
    Then the products should be sorted by name in alphabetical order
