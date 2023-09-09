# Created by mate_ at 8/24/2023
Feature: Display notes
  As a reader
  I want to be able to view other readers' notes
  To check my notes.

  Scenario Outline: My ordered general notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * there are notes <my_general_notes> added by me on <date> date
    When I want to read my notes
    Then it should display my personal notes <my_ordered_general_notes> ordered by date

    Examples:
    | document_title | document_id | username       | my_general_notes                               | date                  | my_ordered_general_notes                       |
    | Clean Code     | 1           | Alice Johnson  | This book changed my life,This part was useful | 2023-01-01,2023-01-02 | This part was useful,This book changed my life |
    | Clean Code     | 1           | David Smith    | Interesting examples,Helpful for projects      | 2023-01-01,2023-01-02 | Interesting examples,Helpful for projects      |
    | OOP Design     | 2           | Alex Carter    | Practical examples,Needs more context          | 2023-01-01,2023-01-02 | Practical examples,Needs more context          |
    | OOP Design     | 2           | Sarah Miller   | Comprehensive coverage,Clear explanation       | 2023-01-01,2023-01-02 | Clear explanation,Comprehensive coverage       |
    | OOP Design     | 2           | Robert Lee     | Step-by-step guide,This part was very clear    | 2023-01-01,2023-01-02 | This part was very clear,Step-by-step guide    |
    | ML Algorithms  | 3           | Julia Chen     | Clear and concise,Pretty repetitive            | 2023-01-01,2023-01-02 | Pretty repetitive,Clear and concise            |


  Scenario Outline: My ordered page notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * there are notes <my_notes> added by me in the page <page_number> on <date> date
    When I want to read my notes in the page <page_number>
    Then it should display my personal notes <my_ordered_notes> ordered by date and favorite

    Examples:
    | document_title | document_id | username        | page_number | my_notes                                           | date                   | my_ordered_notes                                   |
    | Clean Code     | 1           | Alice Johnson   | 1           | Don't forget these concepts,This part was useful   | 2023-01-01, 2023-01-02 | This part was useful,Don't forget these concepts   |
    | Clean Code     | 1           | David Smith     | 2           | Interesting examples here,Helpful for projects     | 2023-01-01, 2023-01-02 | Interesting examples here,Helpful for projects     |
    | Clean Code     | 1           | Emily Brown     | 10          | Insightful example,Needs more context              | 2023-01-01, 2023-01-02 | Insightful example,Needs more context              |
    | OOP Design     | 2           | Alex Carter     | 3           | Practical exercise,Clear explanation               | 2023-01-01, 2023-01-02 | Clear explanation,Practical exercise               |
    | OOP Design     | 2           | Sarah Miller    | 8           | Comprehensive explanation,This part was very clear | 2023-01-01, 2023-01-02 | Comprehensive explanation,This part was very clear |
    | OOP Design     | 2           | Robert Lee      | 12          | Step-by-step guide,Pretty repetitive               | 2023-01-01, 2023-01-02 | Pretty repetitive,Step-by-step guide               |
    | ML Algorithms  | 3           | Julia Chen      | 2           | Clear and concise explanation,Needs more examples  | 2023-01-01, 2023-01-02 | Clear and concise explanation,Needs more examples  |
    | ML Algorithms  | 3           | Michael Wong    | 7           | In-depth analysis,Practical examples               | 2023-01-01, 2023-01-02 | In-depth analysis,Practical examples               |


  Scenario Outline: General notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * I have <followers> followers
    * I am <user_type> user
    * there are general notes <general_notes> added by other users on <date> date marked as <is_favorite> favorite
    When I want to read the general notes
    Then it should display the general notes <ordered_general_notes> ordered by date and favorite

    Examples:
    | document_title | document_id | username      | user_type    | followers | general_notes                                                            | date                   | is_favorite | ordered_general_notes                             |
    | Clean Code     | 1           | alice.johnson | reader       | 1         | Important concepts,Explained well,Not relevant                           | 2023-01-01, 2023-01-02 | 1,0         | Important concepts,Explained well,Not relevant    |
    | Clean Code     | 1           | david.smith   | professor    | 2         | Remember for future projects,Skipped,Interesting                         | 2023-01-01, 2023-01-02 | 0,1         | Skipped,Remember for future projects,Interesting  |
    | OOP Design     | 2           | alex.carter   | professor    | 3         | Missing real-world scenarios,Too theoretical                             | 2023-01-01, 2023-01-02 | 1,0         | Missing real-world scenarios,Too theoretical      |
    | OOP Design     | 2           | sarah.miller  | reader       | 4         | Confusing terminology,Useful diagrams,Too verbose                        | 2023-01-01, 2023-01-02 | 0,1         | Useful diagrams,Confusing terminology,Too verbose |
    | OOP Design     | 2           | robert.lee    | professor    | 5         | Simplified explanations,Repetitive content,Too advanced                  | 2023-01-01, 2023-01-02 | 1,0         | Simplified explanations,Repetitive content        |
    | ML Algorithms  | 3           | julia.chen    | reader       | 6         | Lacks advanced topics,Great for beginners,Too shallow                    | 2023-01-01, 2023-01-02 | 0,1         | Great for beginners,Lacks advanced topics         |
    | ML Algorithms  | 3           | michael.wong  | reader       | 7         | Real-world case studies missing,Well-structured,Requires prior knowledge | 2023-01-01, 2023-01-02 | 1,0         | Real-world case studies missing,Well-structured   |
    | ML Algorithms  | 3           | nicole.patel  | reader       | 8         | Comprehensive resource,Requires more examples,Good references            | 2023-01-01, 2023-01-02 | 0,1         | Requires more examples,Comprehensive resource     |


  Scenario Outline: Page notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * I am <user_type> user
    * I have <followers> followers
    * there are notes <notes> added by other users in the page <page_number> on <date> date marked as <is_favorite> favorite
    When I want to read the notes in the page <page_number>
    Then it should display the notes <ordered_notes> ordered by date and favorite

    Examples:
    | document_title | document_id | username      | user_type | followers | page_number | notes                                                                | date                             | is_favorite | ordered_notes                                                        |
    | Clean Code     | 1           | alice.johnson | reader    | 1         | 1           | Important introduction,Explained well,Not relevant                   | 2023-01-01,2023-01-02,2023-01-03 | 1,0,0       | Not relevant,Explained well,Important introduction                   |
    | Clean Code     | 1           | david.smith   | professor | 2         | 2           | Remember for future projects,Skipped,Interesting                     | 2023-01-01,2023-01-02,2023-01-03 | 0,1,1       | Interesting,Remember for future projects,Skipped                     |
    | Clean Code     | 1           | emily.brown   | professor | 3         | 10          | Important concept,Useful code snippet,Needs more context             | 2023-01-01,2023-01-02,2023-01-03 | 1,0,0       | Needs more context,Important concept,Useful code snippet             |
    | OOP Design     | 2           | alex.carter   | reader    | 4         | 3           | Missing explanation,Well-structured,Too simple                       | 2023-01-01,2023-01-02,2023-01-03 | 0,1,1       | Too simple,Well-structured,Missing explanation                       |
    | OOP Design     | 2           | sarah.miller  | professor | 5         | 8           | Unclear terminology,Great diagram,Advanced content                   | 2023-01-01,2023-01-02,2023-01-03 | 1,0,1       | Advanced content,Unclear terminology,Great diagram                   |
    | OOP Design     | 2           | robert.lee    | reader    | 6         | 12          | Repetitive content,Valuable insights,Not necessary                   | 2023-01-01,2023-01-02,2023-01-03 | 0,1,0       | Valuable insights,Repetitive content,Not necessary                   |
    | ML Algorithms  | 3           | julia.chen    | reader    | 7         | 2           | Lacks real-world examples,Good for beginners,Too shallow             | 2023-01-01,2023-01-02,2023-01-03 | 1,0,1       | Too shallow,Good for beginners,Lacks real-world examples             |
    | ML Algorithms  | 3           | michael.wong  | reader    | 8         | 7           | Missing practical cases,Structured content,Requires prior knowledge  | 2023-01-01,2023-01-02,2023-01-03 | 0,1,1       | Requires prior knowledge,Structured content,Missing practical cases  |
    | ML Algorithms  | 3           | nicole.patel  | professor | 9         | 10          | Needs more practical insights,Good references,Comprehensive resource | 2023-01-01,2023-01-02,2023-01-03 | 1,0,0       | Comprehensive resource,Needs more practical insights,Good references |