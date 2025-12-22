Feature: Login functionality
  
  @login
  Scenario: Successful login with valid credentials
    Given user is on the login page
    When 'standard_user' logs in with valid credentials
    Then user should be logged in successfully
  
  @wip
  Scenario: locked_out_user trying to login
    Given user is on the login page
    When 'locked_out_user' logs in
    Then user is on the login page

  Scenario: user login with invalid credentials
    Given user is on the login page
    When 'standard_user' logs in with wrong password 'abc'
    Then error message should be displayed 'standard_user' 'abc'

    Scenario: user logins with different id's
      Given user is on the login page
      When user enters login details
      | username | password |
      | admin1   | admin123 |
      | admin2   | admin123 |
      | admin3   | admin123 |
      Then API response should be
"""
{
  "status": "success"
}
"""

