# language:en
Feature:
  As a reader
  I want to follow the activities or collections of another reader of my interest as a follow-up
  so that I can easily access the content of other users

  Scenario: Show updates of followed collection
    Given that I follow a collection
    When the owner of the collection adds a new book
    Then the book will appear in my feed

  Scenario:  Follow a reader
    Given that there is a reader Andrés
    And that there is a reader Juan
    When Andrés follows Juan
    Then Juan will appear in the list of following of Andrés
    And Andrés will appear in the list of followers of Juan

  Scenario: Show updates of followed reader
    Given that I follow a reader in my tracked list
    When the reader does a new activity
    Then the activity will appear in the list of recent activities

  Scenario: Follow a collection of other readers
    Given that there is a collection
    When I follow the collection
    Then the new collection will appear in my list of followed collections