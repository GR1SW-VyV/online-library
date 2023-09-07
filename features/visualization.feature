# Created by mate_ at 8/24/2023
Feature: Display notes
  As a reader
  I want to be able to view other readers' notes
  To check my notes.

  Scenario Outline: General notes
    Given I have the document <document_title> with the id <document_id>
    And I am logged in with my username <username>
    And there are my personal general notes <my_general_notes> added by me
    And there are general notes <general_notes> added by other users
    When I want to compare my notes with those of other users
    Then it should display my personal general notes <my_general_notes> ordered
    And the general notes <general_notes> from other users ordered.

    Examples:
    | document_title | document_id | username       | my_general_notes                               | general_notes                                                            |
    | Clean Code     | 1           | Alice Johnson  | This book changed my life,This part was useful | Important concepts,Explained well,Not relevant                           |
    | Clean Code     | 1           | David Smith    | Interesting examples,Helpful for projects      | Remember for future projects,Skipped,Interesting                         |
    | OOP Design     | 2           | Alex Carter    | Practical examples,Needs more context          | Missing real-world scenarios,Too theoretical                             |
    | OOP Design     | 2           | Sarah Miller   | Comprehensive coverage,Clear explanation       | Confusing terminology,Useful diagrams,Too verbose                        |
    | OOP Design     | 2           | Robert Lee     | Step-by-step guide,This part was very clear    | Simplified explanations,Repetitive content,Too advanced                  |
    | ML Algorithms  | 3           | Julia Chen     | Clear and concise,Pretty repetitive            | Lacks advanced topics,Great for beginners,Too shallow                    |
    | ML Algorithms  | 3           | Michael Wong   | In-depth exploration,Needs more examples       | Real-world case studies missing,Well-structured,Requires prior knowledge |
    | ML Algorithms  | 3           | Nicole Patel   | Well-organized content,In-depth analysis       | Comprehensive resource,Requires more examples,Good references            |

  Scenario Outline: Page notes
    Given I have the document <document_title> with the id <document_id>
    And I am logged in with my username <username>
    And there are notes <my_notes> added by me in the page <page_number>
    And there are notes <notes> added by other users in the page <page_number>
    When I want to compare my notes with those of other users in the page <page_number>
    Then it should display my personal notes <my_notes> ordered
    And the notes <notes> from other users ordered.

    Examples:
    | document_title | document_id | username        | page_number | my_notes                                           | notes                                                                |
    | Clean Code     | 1           | Alice Johnson   | 1           | Don't forget these concepts,This part was useful   | Important introduction,Explained well,Not relevant                   |
    | Clean Code     | 1           | David Smith     | 2           | Interesting examples here,Helpful for projects     | Remember for future projects,Skipped this part,Interesting           |
    | Clean Code     | 1           | Emily Brown     | 10          | Insightful example,Needs more context              | Important concept,Useful code snippet,Needs more context             |
    | OOP Design     | 2           | Alex Carter     | 3           | Practical exercise,Clear explanation               | Missing explanation,Well-structured,Too simple                       |
    | OOP Design     | 2           | Sarah Miller    | 8           | Comprehensive explanation,This part was very clear | Unclear terminology,Great diagram,Advanced content                   |
    | OOP Design     | 2           | Robert Lee      | 12          | Step-by-step guide,Pretty repetitive               | Repetitive content,Valuable insights,Not necessary                   |
    | ML Algorithms  | 3           | Julia Chen      | 2           | Clear and concise explanation,Needs more examples  | Lacks real-world examples,Good for beginners,Too shallow             |
    | ML Algorithms  | 3           | Michael Wong    | 7           | In-depth analysis,Practical examples               | Missing practical cases,Structured content,Requires prior knowledge  |
    | ML Algorithms  | 3           | Nicole Patel    | 10          | Well-structured content,In-depth analysis          | Comprehensive resource,Needs more practical insights,Good references |