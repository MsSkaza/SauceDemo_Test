Feature: SauceDemo Product Information

  Scenario: Viewing a product's image
    Given I am on the SauceDemo product page
    When I click on the image of "Sauce Labs Fleece Jacket"
    Then I should see a larger view of the product's image

  Scenario: Viewing a product's description
    Given I am on the SauceDemo product page
    When I click on the "Sauce Labs Fleece Jacket" product name
    Then I should see a detailed description of the "Sauce Labs Fleece Jacket"
