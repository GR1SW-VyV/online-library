# Created by mate_ at 8/24/2023
Feature: Display notes
  As a reader
  I want to be able to view other readers' notes
  To check my notes.


  Scenario Outline: General notes
    Given I have the document <document_title>
    * I am logged in with my username <username>
    * there are general notes <general_notes> added by other users who are <user_types> with <followers> followers on <dates> date
    When I want to read the general notes
    Then it should display the general notes <ordered_general_notes> ordered by date

    Examples:
    | document_title | username       | user_types                    | followers | general_notes                                                            | dates                                              | ordered_general_notes                                                    |
    | Clean Code     | alice.johnson3 | reader,reader,professor       | 1,2,3     | Important concepts,Explained well,Not relevant                           | 2023-01-03 17:18,2023-01-02 07:15,2023-01-01 09:30 | Not relevant,Explained well,Important concepts                           |
    | Clean Code     | david.smith3   | professor,reader,professor    | 2,3,4     | Remember for future projects,Skipped,Interesting                         | 2023-01-03 04:22,2023-01-02 10:05,2023-01-01 03:47 | Interesting,Remember for future projects,Skipped                         |
    | OOP Design     | alex.carter3   | professor,professor,reader    | 3,4,5     | Missing real-world scenarios,Too theoretical,Not interesting             | 2023-01-03 15:11,2023-01-02 01:27,2023-01-01 06:58 | Too theoretical,Missing real-world scenarios,Not interesting             |
    | OOP Design     | sarah.miller3  | reader,professor,reader       | 4,5,6     | Confusing terminology,Useful diagrams,Too verbose                        | 2023-01-03 21:10,2023-01-02 11:52,2023-01-01 08:33 | Useful diagrams,Too verbose,Confusing terminology                        |
    | OOP Design     | robert.lee3    | professor,professor,reader    | 5,6,7     | Simplified explanations,Repetitive content,Too advanced                  | 2023-01-03 13:00,2023-01-02 18:45,2023-01-01 14:59 | Repetitive content,Simplified explanations,Too advanced                  |
    | ML Algorithms  | julia.chen3    | reader,reader,professor       | 6,7,8     | Lacks advanced topics,Great for beginners,Too shallow                    | 2023-01-03 02:50,2023-01-02 05:41,2023-01-01 19:15 | Too shallow,Great for beginners,Lacks advanced topics                    |
    | ML Algorithms  | michael.wong3  | professor,professor,professor | 7,8,9     | Real-world case studies missing,Well-structured,Requires prior knowledge | 2023-01-03 12:38,2023-01-02 22:07,2023-01-01 17:29 | Requires prior knowledge,Well-structured,Real-world case studies missing |
    | ML Algorithms  | nicole.patel3  | professor,reader,reader       | 8,9,10    | Comprehensive resource,Requires more examples,Good references            | 2023-01-03 23:04,2023-01-02 16:20,2023-01-01 20:14 | Comprehensive resource,Good references,Requires more examples            |
    | Clean Code     | emily.brown3   | professor,professor,reader    | 10,10,11  | Needs more context,Important concept,Useful code snippet                 | 2023-01-03 09:54,2023-01-03 14:33,2023-01-01 22:26 | Important concept,Needs more context,Useful code snippet                 |


  Scenario Outline: Page notes
    Given I have the document <document_title>
    * I am logged in with my username <username>
    * there are notes <page_notes> added by other users who are <user_types> with <followers> followers in the page <page_number> on <dates> date marked as <favorites> favorite
    When I want to read the notes in the page <page_number>
    Then it should display the notes <ordered_page_notes> ordered by date and favorite

    Examples:
    | document_title | username       | user_types                    | followers | page_number | page_notes                                                          | dates                                              | favorites   | ordered_page_notes                                                  |
    | Clean Code     | emily.brown4   | professor,professor,reader    | 3,4,5     | 10          | Needs more context,Important concept,Useful code snippet            | 2023-01-03 00:12,2023-01-01 22:59,2023-01-02 05:09 | 0,1,0       | Important concept,Needs more context,Useful code snippet            |
    | OOP Design     | sarah.miller4  | professor,professor,reader    | 5,6,7     | 8           | Advanced content,Unclear terminology,Great diagram                  | 2023-01-03 11:03,2023-01-01 08:50,2023-01-02 16:41 | 1,0,0       | Advanced content,Unclear terminology,Great diagram                  |
    | OOP Design     | alex.carter4   | reader,professor,reader       | 4,5,6     | 3           | Too simple,Well-structured,Missing explanation                      | 2023-01-03 09:14,2023-01-01 23:45,2023-01-02 21:36 | 0,1,1       | Well-structured,Missing explanation,Too simple                      |
    | Clean Code     | david.smith4   | professor,reader,professor    | 2,3,4     | 2           | Interesting,Remember for future projects,Skipped                    | 2023-01-03 07:21,2023-01-01 02:23,2023-01-02 10:26 | 0,0,1       | Skipped,Interesting,Remember for future projects                    |
    | ML Algorithms  | julia.chen4    | professor,professor,professor | 7,8,9     | 2           | Too shallow,Good for beginners,Lacks real-world examples            | 2023-01-03 01:45,2023-01-01 12:48,2023-01-02 03:57 | 1,1,0       | Good for beginners,Too shallow,Lacks real-world examples            |
    | ML Algorithms  | michael.wong4  | professor,reader,reader       | 8,9,10    | 7           | Requires prior knowledge,Structured content,Missing practical cases | 2023-01-03 15:54,2023-01-01 14:37,2023-01-02 19:52 | 1,1,1       | Requires prior knowledge,Missing practical cases,Structured content |
    | OOP Design     | robert.lee4    | reader,reader,professor       | 6,7,8     | 12          | Valuable insights,Repetitive content,Not necessary                  | 2023-01-03 04:38,2023-01-01 13:19,2023-01-02 09:44 | 1,0,1       | Not necessary,Valuable insights,Repetitive content                  |
    | Clean Code     | alice.johnson4 | reader,reader,professor       | 1,2,3     | 1           | Important introduction,Explained well,Not relevant                  | 2023-01-03 06:32,2023-01-01 18:06,2023-01-02 04:20 | 0,0,0       | Not relevant,Explained well,Important introduction                  |
    | ML Algorithms  | nicole.patel4  | professor,reader,reader       | 9,11,11   | 5           | Comprehensive resource,Requires more examples,Good references       | 2023-01-03 13:28,2023-01-01 23:59,2023-01-01 20:15 | 0,1,1       | Comprehensive resource,Requires more examples,Good references       |