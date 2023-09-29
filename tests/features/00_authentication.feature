Feature: User Authentication

  Scenario: Successful login with valid credentials
    Given I am on the SauceDemo login page
    When I login with valid credentials
    Then I should see the inventory page

  Scenario: Failed login with locked credentials
    Given I am on the SauceDemo login page
    When I login with locked credentials
    Then I should see an error message about locked user

  Scenario: Failed login with invalid credentials
    Given I am on the SauceDemo login page
    When I login with invalid credentials
    Then I should see an error message about invalid user

  Scenario: Logout from SauceDemo
    Given I am logged in to SauceDemo
    When I click the logout button
    Then I should be redirected to the login page
