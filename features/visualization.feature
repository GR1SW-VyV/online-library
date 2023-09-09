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
    | Clean Code     | 1           | David Smith    | Interesting examples,Helpful for projects      | 2023-01-01,2023-01-02 | Helpful for projects,Interesting examples      |
    | OOP Design     | 2           | Alex Carter    | Practical examples,Needs more context          | 2023-02-01,2023-01-02 | Practical examples,Needs more context          |
    | OOP Design     | 2           | Sarah Miller   | Comprehensive coverage,Clear explanation       | 2023-01-01,2023-01-10 | Clear explanation,Comprehensive coverage       |
    | OOP Design     | 2           | Robert Lee     | Step-by-step guide,This part was very clear    | 2023-07-11,2023-01-02 | Step-by-step guide,This part was very clear    |
    | ML Algorithms  | 3           | Julia Chen     | Clear and concise,Pretty repetitive            | 2023-01-01,2023-01-02 | Pretty repetitive,Clear and concise            |


  Scenario Outline: My ordered page notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * there are notes <my_page_notes> added by me in the page <page_number> on <date> date marked as <is_favorite> favorite
    When I want to read my notes in the page <page_number>
    Then it should display my personal notes <my_ordered_page_notes> ordered by date and favorite

    Examples:
    | document_title | document_id | username        | page_number | my_page_notes                                      | is_favorite | date                  | my_ordered_page_notes                              |
    | Clean Code     | 1           | Alice Johnson   | 1           | Don't forget these concepts,This part was useful   | 1,1         | 2023-01-01,2023-01-02 | This part was useful,Don't forget these concepts   |
    | Clean Code     | 1           | David Smith     | 2           | Interesting examples here,Helpful for projects     | 0,0         | 2023-01-03,2023-01-01 | Interesting examples here,Helpful for projects     |
    | Clean Code     | 1           | Emily Brown     | 10          | Insightful example,Needs more context              | 0,0         | 2023-01-01,2023-01-09 | Needs more context,Insightful example              |
    | OOP Design     | 2           | Alex Carter     | 3           | Practical exercise,Clear explanation               | 1,0         | 2023-01-01,2023-01-01 | Practical exercise,Clear explanation               |
    | OOP Design     | 2           | Sarah Miller    | 8           | Comprehensive explanation,This part was very clear | 0,1         | 2023-03-02,2023-03-02 | This part was very clear,Comprehensive explanation |
    | OOP Design     | 2           | Robert Lee      | 12          | Step-by-step guide,Pretty repetitive               | 1,0         | 2023-01-01,2023-01-02 | Step-by-step guide,Pretty repetitive               |
    | ML Algorithms  | 3           | Julia Chen      | 2           | Clear and concise explanation,Needs more examples  | 0,1         | 2023-01-01,2023-01-02 | Needs more examples,Clear and concise explanation  |
    | ML Algorithms  | 3           | Michael Wong    | 7           | In-depth analysis,Practical examples               | 1,0         | 2023-01-01,2023-01-02 | In-depth analysis,Practical examples               |


  Scenario Outline: General notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * there are general notes <general_notes> added by other users who are <user_type> with <followers> followers on <date> date
    When I want to read the general notes
    Then it should display the general notes <ordered_general_notes> ordered by date

    Examples:
    | document_title | document_id | username      | user_type                     | followers | general_notes                                                            | date                             | ordered_general_notes                                                    |
    | Clean Code     | 1           | alice.johnson | reader,reader,professor       | 1,2,3     | Important concepts,Explained well,Not relevant                           | 2023-01-03,2023-01-02,2023-01-01 | Not relevant,Explained well,Important concepts                           |
    | Clean Code     | 1           | david.smith   | professor,reader,professor    | 2,3,4     | Remember for future projects,Skipped,Interesting                         | 2023-01-03,2023-01-02,2023-01-01 | Interesting,Remember for future projects,Skipped                         |
    | OOP Design     | 2           | alex.carter   | professor,professor,reader    | 3,4,5     | Missing real-world scenarios,Too theoretical,Not interesting             | 2023-01-03,2023-01-02,2023-01-01 | Too theoretical,Missing real-world scenarios,Not interesting             |
    | OOP Design     | 2           | sarah.miller  | reader,professor,reader       | 4,5,6     | Confusing terminology,Useful diagrams,Too verbose                        | 2023-01-03,2023-01-02,2023-01-01 | Useful diagrams,Too verbose,Confusing terminology                        |
    | OOP Design     | 2           | robert.lee    | professor,professor,reader    | 5,6,7     | Simplified explanations,Repetitive content,Too advanced                  | 2023-01-03,2023-01-02,2023-01-01 | Repetitive content,Simplified explanations,Too advanced                  |
    | ML Algorithms  | 3           | julia.chen    | reader,reader,professor       | 6,7,8     | Lacks advanced topics,Great for beginners,Too shallow                    | 2023-01-03,2023-01-02,2023-01-01 | Too shallow,Great for beginners,Lacks advanced topics                    |
    | ML Algorithms  | 3           | michael.wong  | professor,professor,professor | 7,8,9     | Real-world case studies missing,Well-structured,Requires prior knowledge | 2023-01-03,2023-01-02,2023-01-01 | Requires prior knowledge,Well-structured,Real-world case studies missing |
    | ML Algorithms  | 3           | nicole.patel  | professor,reader,reader       | 8,9,10    | Comprehensive resource,Requires more examples,Good references            | 2023-01-03,2023-01-02,2023-01-01 | Comprehensive resource,Good references,Requires more examples            |



  Scenario Outline: Page notes
    Given I have the document <document_title> with the id <document_id>
    * I am logged in with my username <username>
    * there are notes <page_notes> added by other users who are <user_type> with <followers> followers in the page <page_number> on <date> date marked as <is_favorite> favorite
    When I want to read the notes in the page <page_number>
    Then it should display the notes <ordered_page_notes> ordered by date and favorite

    Examples:
    | document_title | document_id | username      | user_type                     | followers | page_number | page_notes                                                          | date                             | is_favorite | ordered_page_notes                                                  |
    | Clean Code     | 1           | emily.brown   | professor,professor,reader    | 3,4,5     | 10          | Needs more context,Important concept,Useful code snippet            | 2023-01-03,2023-01-01,2023-01-02 | 0,1,0       | Important concept,Needs more context,Useful code snippet            |
    | OOP Design     | 2           | sarah.miller  | professor,professor,reader    | 5,6,7     | 8           | Advanced content,Unclear terminology,Great diagram                  | 2023-01-03,2023-01-01,2023-01-02 | 1,0,0       | Advanced content,Unclear terminology,Great diagram                  |
    | OOP Design     | 2           | alex.carter   | reader,professor,reader       | 4,5,6     | 3           | Too simple,Well-structured,Missing explanation                      | 2023-01-03,2023-01-01,2023-01-02 | 0,1,1       | Well-structured,Missing explanation,Too simple                      |
    | Clean Code     | 1           | david.smith   | professor,reader,professor    | 2,3,4     | 2           | Interesting,Remember for future projects,Skipped                    | 2023-01-03,2023-01-01,2023-01-02 | 0,0,1       | Skipped,Interesting,Remember for future projects                    |
    | ML Algorithms  | 3           | julia.chen    | professor,professor,professor | 7,8,9     | 2           | Too shallow,Good for beginners,Lacks real-world examples            | 2023-01-03,2023-01-01,2023-01-02 | 1,1,0       | Good for beginners,Too shallow,Lacks real-world examples            |
    | ML Algorithms  | 3           | michael.wong  | professor,reader,reader       | 8,9,10    | 7           | Requires prior knowledge,Structured content,Missing practical cases | 2023-01-03,2023-01-01,2023-01-02 | 1,1,1       | Requires prior knowledge,Missing practical cases,Structured content |
    | OOP Design     | 2           | robert.lee    | reader,reader,professor       | 6,7,8     | 12          | Valuable insights,Repetitive content,Not necessary                  | 2023-01-03,2023-01-01,2023-01-02 | 1,0,1       | Not necessary,Valuable insights,Repetitive content                  |
    | Clean Code     | 1           | alice.johnson | reader,reader,professor       | 1,2,3     | 1           | Important introduction,Explained well,Not relevant                  | 2023-01-03,2023-01-01,2023-01-02 | 0,0,0       | Not relevant,Explained well,Important introduction                  |
