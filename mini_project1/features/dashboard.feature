Feature: Dashboard functionality
  
  Scenario: Remove items when no item is added
    Given user is logged in
    When user remove 'Sauce Labs Backpack' from the inventory
    Then cart badge should be updated correctly

  Scenario: Add one item when all items are added already 
    Given user is logged in
    When user adds 6 products to the dashboard cart
    Then add 'Sauce Labs Backpack' to inventory
    Then cart badge should be updated correctly

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

  Scenario: Remove items by their name
    Given user is logged in
    When user adds 6 products to the dashboard cart
    When user remove 'Sauce Labs Backpack' from the inventory
    Then cart badge should be updated correctly

  Scenario Outline: Sort items alphabetically
    Given user is logged in
    When user sorts items "<order>"
    Then items should be sorted "<order>"

    Examples:
      | order      |
      | ascending  |
      | descending |