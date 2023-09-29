Feature: SauceDemo Checkout Process

  Scenario: Continue shopping from the cart
    Given I am viewing my cart on SauceDemo
    When I click on the "Continue Shopping" button
    Then I should return to the product page

  Scenario: Failed checkout due to missing information
    Given I am on the SauceDemo checkout page
    When I enter an empty first name
    And I enter a last name "Doe"
    And I enter a postal code "12345"
    And I click the continue button
    Then I should see an error message indicating the first name is required

  Scenario: Successful checkout process
    Given I am on the SauceDemo checkout page
    When I enter a first name "John"
    And I enter a last name "Doe"
    And I enter a postal code "12345"
    And I click the continue button
    And I confirm my purchase
    Then I should see a thank you confirmation message
