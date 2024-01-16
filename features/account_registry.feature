Feature: Account registry


  Scenario: User is able to create a new account
    Given Number of accounts in registry equals: "0"
    When I create an account using name: "kurt", last name: "cobain", pesel: "59080926735"
    Then Number of accounts in registry equals: "1"
    And Account with pesel "59080926735" exists in registry


  Scenario: User is able to create a second account
    Given Number of accounts in registry equals: "1"
    When I create an account using name: "john", last name: "lennon", pesel: "64022388722"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "64022388722" exists in registry


  Scenario: Admin user is able to save the account registry
    When I save the account registry
    Then Number of accounts in registry equals: "2"

  Scenario: Add test account
    Given Number of accounts in registry equals: "2"
    When I create an account using name: "test", last name: "test", pesel: "74081211259"
    Then Number of accounts in registry equals: "3"
    And Account with pesel "74081211259" exists in registry

  Scenario: User is able to delete already created account
    Given Account with pesel "74081211259" exists in registry
    When I delete account with pesel: "74081211259"
    Then Account with pesel "74081211259" does not exist in registry


  Scenario: User is able to update last name saved in account
    Given Account with pesel "64022388722" exists in registry
    When I update last name to "krupa" for account with pesel: "64022388722"
    Then Last name in account with pesel "64022388722" is "krupa"


  Scenario: User is able to load account registry
    Given Number of accounts in registry equals: "2"
    When I load the account registry
    And Account with pesel "59080926735" exists in registry
    And Account with pesel "64022388722" exists in registry


  Scenario: User is able to delete both accounts
    Given Account with pesel "59080926735" exists in registry
    And Account with pesel "64022388722" exists in registry
    When I delete account with pesel: "59080926735"
    And I delete account with pesel: "64022388722"
    Then Account with pesel "59080926735" does not exist in registry
    And Account with pesel "64022388722" does not exist in registry
