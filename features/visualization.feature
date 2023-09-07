# Created by mate_ at 8/24/2023
Feature: Display notes
  As a reader
  I want to be able to view other readers' notes
  To check my notes.

  Scenario Outline: General notes
    Given I have the book <book_id>
    And I am logged in with my username <username>
    When I am reading the details of the book
    Then it should display my personal general notes <my_general_notes>
    And the general notes <general_notes> from other users ordered by their number of followers.

    Examples:
    | book_id | username       | my_general_notes            | general_notes                                                            |
    | 1       | Alice Johnson  | This book changed my life   | Important concepts,Explained well,Not relevant                           |
    | 1       | David Smith    | Interesting examples        | Remember for future projects,Skipped,Interesting                         |
    | 2       | Alex Carter    | Practical examples          | Missing real-world scenarios,Too theoretical                             |
    | 2       | Sarah Miller   | Comprehensive coverage      | Confusing terminology,Useful diagrams,Too verbose                        |
    | 2       | Robert Lee     | Step-by-step guide          | Simplified explanations,Repetitive content,Too advanced                  |
    | 3       | Julia Chen     | Clear and concise           | Lacks advanced topics,Great for beginners,Too shallow                    |
    | 3       | Michael Wong   | In-depth exploration        | Real-world case studies missing,Well-structured,Requires prior knowledge |
    | 3       | Nicole Patel   | Well-organized content      | Comprehensive resource,Requires more examples,Good references            |

   Scenario Outline: Page notes
     Given I have the book <book_id>
     And I am logged in with my username <username>
     When I am reading the page <page_number>
     Then it should display my personal notes <my_notes>
     And the notes <notes> from other users ordered by their number of followers.

     Examples:
     | book_id | username        | page_number | my_notes                      | notes                                                                |
     | 1       | Alice Johnson   | 1           | Don't forget these concepts   | Important introduction,Explained well,Not relevant                   |
     | 1       | David Smith     | 2           | Interesting examples here     | Remember for future projects,Skipped this part,Interesting           |
     | 1       | Emily Brown     | 10          | Insightful example            | Important concept,Useful code snippet,Needs more context             |
     | 2       | Alex Carter     | 3           | Practical exercise            | Missing explanation,Well-structured,Too simple                       |
     | 2       | Sarah Miller    | 8           | Comprehensive explanation     | Unclear terminology,Great diagram,Advanced content                   |
     | 2       | Robert Lee      | 12          | Step-by-step guide            | Repetitive content,Valuable insights,Not necessary                   |
     | 3       | Julia Chen      | 2           | Clear and concise explanation | Lacks real-world examples,Good for beginners,Too shallow             |
     | 3       | Michael Wong    | 7           | In-depth analysis             | Missing practical cases,Structured content,Requires prior knowledge  |
     | 3       | Nicole Patel    | 10          | Well-structured content       | Comprehensive resource,Needs more practical insights,Good references |