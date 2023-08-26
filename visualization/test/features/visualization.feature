# Created by mate_ at 8/24/2023
Feature: Display annotations
  As a reader
  I want to be able to view other readers' annotations
  To check my annotations.

  #Scenario: Section annotations
  #  Given a book with 5 annotations of 3 different users in 2 different sections
  #  When I am on the section 7
  #  Then it should display 3 annotations of other users and 2 of mine

  Scenario: Book reviews
    Given the book Clean Code
    When I am reviewing the details of the book
    #Then it should display 5 annotations of the book from 5 other readers
    Then it should display the following reviews:
      | user             | date       | content                      |
      | Marcela Tapia    | 21-03-2023 | A must-read for programmers! |
      | Bryan Montalvo   | 07-04-2023 | Great insights and examples. |
      | Adamaris Diaz    | 14-05-2023 | Practical advice for coding. |
      | Mateo Gavilanez  | 15-06-2023 | Well-organized and helpful.  |
      | Cristopher Perez | 04-07-2023 | Changed how I write code.    |

  #Scenario: Page annotations
  #  Given a book with <number_of_annotations> annotations of 3 different users in 2 different pages
  #  When I am reading the page <page_number>
  #  Then it should display 3 annotations of other users and 2 of mine

  Scenario: Page notes
    Given the book Clean Code
    When I am reading the page <page_number>
    Then it should display the following notes:
      | user             | page_number | date       | is_important | content                        |
      | Marcela Tapia    | 1           | 21-03-2023 | True         | Important introduction points. |
      | Bryan Montalvo   | 1           | 07-04-2023 | False        | Interesting examples here.     |
      | Adamaris Diaz    | 1           | 14-05-2023 | True         | Don't forget these concepts.   |
      | Mateo Gavilanez  | 1           | 15-06-2023 | False        | Helpful insights on page 1.    |
      | Cristopher Perez | 1           | 04-07-2023 | False        | Noted down a few tips.         |
      | Marcela Tapia    | 2           | 21-03-2023 | False        | Explained well on page 2.      |
      | Bryan Montalvo   | 2           | 07-04-2023 | True         | Important details here.        |
      | Adamaris Diaz    | 2           | 14-05-2023 | False        | Skipped this part.             |
      | Mateo Gavilanez  | 2           | 15-06-2023 | False        | Not relevant for me.           |
      | Cristopher Perez | 2           | 04-07-2023 | True         | Remember for future projects.  |