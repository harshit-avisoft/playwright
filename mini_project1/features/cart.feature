Feature: Cart functionality

  Scenario: Add product to cart
    Given I am logged in
    When I add a product to cart
    Then the product should appear in the cart
