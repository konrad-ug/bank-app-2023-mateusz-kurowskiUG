@bdd_transfers
Feature: BDD Transfers tests

    Scenario: User is able to receive valid transfer
        Given User's balance equals: 0
        When User receives a transfer: 10
        Then User's history equals: [10]
        And User's balance equals: 10

    Scenario: User is not able to receive invalid transfer
        Given User's balance equals: 0
        When User receives a transfer: -10
        Then User's history equals: []
        And User's balance equals: 0

    Scenario: User is not able to receive invalid transfer2
        Given User's balance equals: 0
        When User receives a transfer: 0
        Then User's history equals: []
        And User's balance equals: 0

    Scenario: User is able to perform outgoing valid transfer with enough money
        Given User's balance equals: 100
        When User sends a transfer: 100
        Then User's history equals: [-100]
        And User's balance equals: 0

    Scenario: User is able to perform outgoing valid transfer with enough money
        Given User's balance equals: 100
        When User sends a transfer: 50
        Then User's history equals: [-50]
        And User's balance equals: 50

    Scenario: User is not able to perform outgoing valid transfer without money
        Given User's balance equals: 0
        When User sends a transfer: 1
        Then User's history equals: []
        And User's balance equals: 0

    Scenario: User is not able to perform outgoing invalid transfer
        Given User's balance equals: 100
        When User sends a transfer: -1
        Then User's history equals: []
        And User's balance equals: 100

    Scenario: User is not able to perform outgoing invalid transfer2
        Given User's balance equals: 100
        When User sends a transfer: 0
        Then User's history equals: []
        And User's balance equals: 100
