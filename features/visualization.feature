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
    And the general annotations <general_annotations> from other users ordered by their number of followers.

    Examples:
    | book             | book_id | username       | my_general_annotations      | general_annotations                                                      |
    | Clean Code       | 1       | Alice Johnson  | This book changed my life   | Important concepts,Explained well,Not relevant                           |
    | Clean Code       | 1       | David Smith    | Interesting examples        | Remember for future projects,Skipped,Interesting                         |
    | OOP Design       | 2       | Alex Carter    | Practical examples          | Missing real-world scenarios,Too theoretical                             |
    | OOP Design       | 2       | Sarah Miller   | Comprehensive coverage      | Confusing terminology,Useful diagrams,Too verbose                        |
    | OOP Design       | 2       | Robert Lee     | Step-by-step guide          | Simplified explanations,Repetitive content,Too advanced                  |
    | Machine Learning | 3       | Julia Chen     | Clear and concise           | Lacks advanced topics,Great for beginners,Too shallow                    |
    | Machine Learning | 3       | Michael Wong   | In-depth exploration        | Real-world case studies missing,Well-structured,Requires prior knowledge |
    | Machine Learning | 3       | Nicole Patel   | Well-organized content      | Comprehensive resource,Requires more examples,Good references            |

   Scenario Outline: Page annotations
     Given I have the book <book> with the id <book_id>
     And I am logged in with my username <username>
     When I am reading the page <page_number>
     Then it should display my personal annotations <my_annotations>
     And the annotations <annotations> from other users ordered by their number of followers.

     Examples:
     | book          | book_id | username        | page_number | my_annotations                | annotations                                                          |
     | Clean Code    | 1       | Alice Johnson   | 1           | Don't forget these concepts   | Important introduction,Explained well,Not relevant                   |
     | Clean Code    | 1       | David Smith     | 2           | Interesting examples here     | Remember for future projects,Skipped this part,Interesting           |
     | Clean Code    | 1       | Emily Brown     | 10          | Insightful example            | Important concept,Useful code snippet,Needs more context             |
     | OOP Design    | 2       | Alex Carter     | 3           | Practical exercise            | Missing explanation,Well-structured,Too simple                       |
     | OOP Design    | 2       | Sarah Miller    | 8           | Comprehensive explanation     | Unclear terminology,Great diagram,Advanced content                   |
     | OOP Design    | 2       | Robert Lee      | 12          | Step-by-step guide            | Repetitive content,Valuable insights,Not necessary                   |
     | ML Algorithms | 3       | Julia Chen      | 2           | Clear and concise explanation | Lacks real-world examples,Good for beginners,Too shallow             |
     | ML Algorithms | 3       | Michael Wong    | 7           | In-depth analysis             | Missing practical cases,Structured content,Requires prior knowledge  |
     | ML Algorithms | 3       | Nicole Patel    | 10          | Well-structured content       | Comprehensive resource,Needs more practical insights,Good references |