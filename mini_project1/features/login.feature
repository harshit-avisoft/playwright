Feature: Login functionality

  Scenario: Valid user login
    Given I open the login page
    When I login with valid credentials
    Then I should see the dashboard
