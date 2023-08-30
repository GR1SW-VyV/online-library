# Created by mate_ at 8/24/2023
Feature: Display annotations
  As a reader
  I want to be able to view other readers' annotations
  To check my annotations.

  Scenario Outline: General annotations
    Given I have the book <book> with the id <book_id>
    And I am logged in with my username <username>
    When I am reading the details of the book
    Then it should display my personal general annotations <my_general_annotations>
    And the general annotattions <general_annotations> from other users ordered by their number of followers.

    Examples:
    | book       | book_id | username       | my_general_annotations      | general_annotations                              |
    | Clean Code | 1       | Marcela Tapia  | This book changed my life   | Important concepts,Explained well,Not relevant   |
    | Clean Code | 1       | Bryan Montalvo | Interesting examples        | Remember for future projects,Skipped,Interesting |

   Scenario Outline: Page annotations
     Given I have the book <book> with the id <book_id>
     And I am logged in with my username <username>
     When I am reading the page <page_number>
     Then it should display my personal annotations <my_annotations>
     And the annotations <annotations> from other users ordered by their number of followers.

     Examples:
     | book       | book_id | username       | page_number | my_annotations              | annotations                                                |
     | Clean Code | 1       | Marcela Tapia  | 1           | Don't forget these concepts | Important introduction,Explained well,Not relevant         |
     | Clean Code | 1       | Bryan Montalvo | 2           | Interesting examples here   | Remember for future projects,Skipped this part,Interesting |