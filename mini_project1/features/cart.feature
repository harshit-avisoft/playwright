@smoke
Feature: Cart functionality
  @smoke @cart
  Scenario: Verify cart item count
    Given user navigates to cart page
    When user has 2 products in the cart
    Then cart items count should match badge count

  Scenario: Checkout from cart
    Given user has 1 product in the cart
    When user proceeds to checkout
    Then checkout page should be displayed
 