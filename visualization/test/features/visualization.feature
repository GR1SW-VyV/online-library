# Created by mate_ at 8/24/2023
Feature: Display annotations
  As a reader
  I want to be able to view other readers' annotations
  To check my annotations.

  Scenario: Section annotations
    Given a book with 5 annotations of 3 different users in 2 different sections
    When I am on the section 7
    Then it should display 3 annotations of other users and 2 of mine

  Scenario: Book annotations
    Given the book Clean Code
    When I am reviewing the details of the book
    Then it should display 5 annotations of the book from 5 other readers

  Scenario: Page annotations
    Given a book with 5 annotations of 3 different users in 2 different pages
    When I am reading the page 29
    Then it should display 3 annotations of other users and 2 of mine