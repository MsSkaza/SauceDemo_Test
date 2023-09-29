Feature: SauceDemo Cart Functionality

  Scenario: View cart from product page
    Given I have items in my cart
    When I click on the cart icon from the product page
    Then I should be redirected to the cart page to view my items

  Scenario: Checkout from cart page
    Given I have items in my cart
    When I click on the checkout button on the cart page
    Then I should be redirected to the checkout information page
