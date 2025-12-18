Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user logs in with valid credentials
    Then user should be logged in successfully
