# Created by mate_ at 8/24/2023
Feature: Display notes
  As a reader
  I want to be able to view other readers' notes
  To check my notes.

  Scenario Outline: My ordered general notes
    Given I have the document <document_title> 
    * I am logged in with my username <username>
    * there are notes <my_general_notes> added by me on <dates> date
    When I want to read my notes
    Then it should display my personal notes <my_ordered_general_notes> ordered by date

    Examples:
    | document_title | username       | my_general_notes                               | dates                 | my_ordered_general_notes                       |
    | Clean Code     | Alice Johnson1 | This book changed my life,This part was useful | 2023-01-01,2023-01-02 | This part was useful,This book changed my life |
    | Clean Code     | David Smith1   | Interesting examples,Helpful for projects      | 2023-01-01,2023-01-02 | Helpful for projects,Interesting examples      |
    | OOP Design     | Alex Carter1   | Practical examples,Needs more context          | 2023-02-01,2023-01-02 | Practical examples,Needs more context          |
    | OOP Design     | Sarah Miller1  | Comprehensive coverage,Clear explanation       | 2023-01-01,2023-01-10 | Clear explanation,Comprehensive coverage       |
    | OOP Design     | Robert Lee1    | Step-by-step guide,This part was very clear    | 2023-07-11,2023-01-02 | Step-by-step guide,This part was very clear    |
    | ML Algorithms  | Julia Chen1    | Clear and concise,Pretty repetitive            | 2023-01-01,2023-01-02 | Pretty repetitive,Clear and concise            |


  Scenario Outline: My ordered page notes
    Given I have the document <document_title>
    * I am logged in with my username <username>
    * there are notes <my_page_notes> added by me in the page <page_number> on <dates> date marked as <favorites> favorite
    When I want to read my notes in the page <page_number>
    Then it should display my personal notes <my_ordered_page_notes> ordered by date and favorite

    Examples:
    | document_title | username        | page_number | my_page_notes                                      | favorites   | dates                 | my_ordered_page_notes                              |
    | Clean Code     | Alice Johnson2  | 1           | Don't forget these concepts,This part was useful   | 1,1         | 2023-01-01,2023-01-02 | This part was useful,Don't forget these concepts   |
    | Clean Code     | David Smith2    | 2           | Interesting examples here,Helpful for projects     | 0,0         | 2023-01-03,2023-01-01 | Interesting examples here,Helpful for projects     |
    | Clean Code     | Emily Brown2    | 10          | Insightful example,Needs more context              | 0,0         | 2023-01-01,2023-01-09 | Needs more context,Insightful example              |
    | OOP Design     | Alex Carter2    | 3           | Practical exercise,Clear explanation               | 1,0         | 2023-01-01,2023-01-01 | Practical exercise,Clear explanation               |
    | OOP Design     | Sarah Miller2   | 8           | Comprehensive explanation,This part was very clear | 0,1         | 2023-03-02,2023-03-02 | This part was very clear,Comprehensive explanation |
    | OOP Design     | Robert Lee2     | 12          | Step-by-step guide,Pretty repetitive               | 1,0         | 2023-01-01,2023-01-02 | Step-by-step guide,Pretty repetitive               |
    | ML Algorithms  | Julia Chen2     | 2           | Clear and concise explanation,Needs more examples  | 0,1         | 2023-01-01,2023-01-02 | Needs more examples,Clear and concise explanation  |
    | ML Algorithms  | Michael Wong2   | 7           | In-depth analysis,Practical examples               | 1,0         | 2023-01-01,2023-01-02 | In-depth analysis,Practical examples               |


  Scenario Outline: General notes
    Given I have the document <document_title>
    * I am logged in with my username <username>
    * there are general notes <general_notes> added by other users who are <user_types> with <followers> followers on <dates> date
    When I want to read the general notes
    Then it should display the general notes <ordered_general_notes> ordered by date

    Examples:
    | document_title | username       | user_types                    | followers | general_notes                                                            | dates                            | ordered_general_notes                                                    |
    | Clean Code     | alice.johnson3 | reader,reader,professor       | 1,2,3     | Important concepts,Explained well,Not relevant                           | 2023-01-03,2023-01-02,2023-01-01 | Not relevant,Explained well,Important concepts                           |
    | Clean Code     | david.smith3   | professor,reader,professor    | 2,3,4     | Remember for future projects,Skipped,Interesting                         | 2023-01-03,2023-01-02,2023-01-01 | Interesting,Remember for future projects,Skipped                         |
    | OOP Design     | alex.carter3   | professor,professor,reader    | 3,4,5     | Missing real-world scenarios,Too theoretical,Not interesting             | 2023-01-03,2023-01-02,2023-01-01 | Too theoretical,Missing real-world scenarios,Not interesting             |
    | OOP Design     | sarah.miller3  | reader,professor,reader       | 4,5,6     | Confusing terminology,Useful diagrams,Too verbose                        | 2023-01-03,2023-01-02,2023-01-01 | Useful diagrams,Too verbose,Confusing terminology                        |
    | OOP Design     | robert.lee3    | professor,professor,reader    | 5,6,7     | Simplified explanations,Repetitive content,Too advanced                  | 2023-01-03,2023-01-02,2023-01-01 | Repetitive content,Simplified explanations,Too advanced                  |
    | ML Algorithms  | julia.chen3    | reader,reader,professor       | 6,7,8     | Lacks advanced topics,Great for beginners,Too shallow                    | 2023-01-03,2023-01-02,2023-01-01 | Too shallow,Great for beginners,Lacks advanced topics                    |
    | ML Algorithms  | michael.wong3  | professor,professor,professor | 7,8,9     | Real-world case studies missing,Well-structured,Requires prior knowledge | 2023-01-03,2023-01-02,2023-01-01 | Requires prior knowledge,Well-structured,Real-world case studies missing |
    | ML Algorithms  | nicole.patel3  | professor,reader,reader       | 8,9,10    | Comprehensive resource,Requires more examples,Good references            | 2023-01-03,2023-01-02,2023-01-01 | Comprehensive resource,Good references,Requires more examples            |



  Scenario Outline: Page notes
    Given I have the document <document_title>
    * I am logged in with my username <username>
    * there are notes <page_notes> added by other users who are <user_types> with <followers> followers in the page <page_number> on <dates> date marked as <favorites> favorite
    When I want to read the notes in the page <page_number>
    Then it should display the notes <ordered_page_notes> ordered by date and favorite

    Examples:
    | document_title | username       | user_types                    | followers | page_number | page_notes                                                          | dates                            | favorites   | ordered_page_notes                                                  |
    | Clean Code     | emily.brown4   | professor,professor,reader    | 3,4,5     | 10          | Needs more context,Important concept,Useful code snippet            | 2023-01-03,2023-01-01,2023-01-02 | 0,1,0       | Important concept,Needs more context,Useful code snippet            |
    | OOP Design     | sarah.miller4  | professor,professor,reader    | 5,6,7     | 8           | Advanced content,Unclear terminology,Great diagram                  | 2023-01-03,2023-01-01,2023-01-02 | 1,0,0       | Advanced content,Unclear terminology,Great diagram                  |
    | OOP Design     | alex.carter4   | reader,professor,reader       | 4,5,6     | 3           | Too simple,Well-structured,Missing explanation                      | 2023-01-03,2023-01-01,2023-01-02 | 0,1,1       | Well-structured,Missing explanation,Too simple                      |
    | Clean Code     | david.smith4   | professor,reader,professor    | 2,3,4     | 2           | Interesting,Remember for future projects,Skipped                    | 2023-01-03,2023-01-01,2023-01-02 | 0,0,1       | Skipped,Interesting,Remember for future projects                    |
    | ML Algorithms  | julia.chen4    | professor,professor,professor | 7,8,9     | 2           | Too shallow,Good for beginners,Lacks real-world examples            | 2023-01-03,2023-01-01,2023-01-02 | 1,1,0       | Good for beginners,Too shallow,Lacks real-world examples            |
    | ML Algorithms  | michael.wong4  | professor,reader,reader       | 8,9,10    | 7           | Requires prior knowledge,Structured content,Missing practical cases | 2023-01-03,2023-01-01,2023-01-02 | 1,1,1       | Requires prior knowledge,Missing practical cases,Structured content |
    | OOP Design     | robert.lee4    | reader,reader,professor       | 6,7,8     | 12          | Valuable insights,Repetitive content,Not necessary                  | 2023-01-03,2023-01-01,2023-01-02 | 1,0,1       | Not necessary,Valuable insights,Repetitive content                  |
    | Clean Code     | alice.johnson4 | reader,reader,professor       | 1,2,3     | 1           | Important introduction,Explained well,Not relevant                  | 2023-01-03,2023-01-01,2023-01-02 | 0,0,0       | Not relevant,Explained well,Important introduction                  |
