Feature: SauceDemo Footer Information

  Scenario: Navigating to Twitter from footer
    Given I am on any page of SauceDemo
    When I click on the Twitter icon in the footer
    Then I should be redirected to the Sauce Labs Twitter page

  Scenario: Navigating to Facebook from footer
    Given I am on any page of SauceDemo
    When I click on the Facebook icon in the footer
    Then I should be redirected to the Sauce Labs Facebook page

  Scenario: Navigating to Linkedin from footer
    Given I am on any page of SauceDemo
    When I click on the Linkedin icon in the footer
    Then I should be redirected to the Sauce Labs Linkedin page
