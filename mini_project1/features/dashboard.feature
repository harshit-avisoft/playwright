Feature: Dashboard functionality

  Scenario: Add items to cart from dashboard
    Given user is logged in
    When user adds 3 products to the dashboard cart
    Then cart badge should be updated correctly

  Scenario: Remove items from cart from dashboard
    Given user has 3 products in the dashboard cart
    When user removes 2 product from the cart
    Then cart badge should be updated correctly
  
  Scenario: Add items by their name
    Given user is logged in
    When add 'Sauce Labs Backpack' to inventory
    And add 'Sauce Labs Bike Light' to inventory
    Then cart badge should be updated correctly