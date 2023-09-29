Feature: User Profile Management at SauceDemo

  Scenario: Accessing user profile
    Given I am logged in to SauceDemo
    When I click on the user icon
    Then I should see the user profile dropdown options

  Scenario: Reset app state
    Given I am on any page of SauceDemo with modified settings
    When I click on the "Reset App State" option in the profile dropdown
    Then all settings should return to their default state

  Scenario: Navigating to About section
    Given I am logged in to SauceDemo
    When I click on the "About" option in the profile dropdown
    Then I should be redirected to the "About" section of SauceDemo
