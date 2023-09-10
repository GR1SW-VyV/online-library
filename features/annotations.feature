# Created by leoasitimbaya at 24/8/2023
Feature: Write notes

  As a reader I want to make notes in a document to synthesize and facilitate my learning.

  Scenario Template: Take notes of a page of a document
    Given I am reading a document <document_title>
    When I add a note with the text <text> in the page <page_number>
    Then I should see the note in the notes section of the page <page_number>

    Examples:
      |      document_title      | text                                |  page_number |
      | Lean Software            | Tomar en cuenta estos principios    | 1            |
      | Math Book                | Estudiar esto                       | 0            |
      | Physics Book             |                                     | 1000         |

  Scenario Template: Take notes of a document
    Given I am seeing the document information about a document <document_title>
    When I add an note with the text <text>
    Then I should see the note with the information of the document <document_title>

    Examples:
      |      document_title      | text                                |
      | Lean Software            | Tomar en cuenta estos principios    |
      | Math Book                | Estudiar esto                       |
      | Physics Book             |                            |




  Scenario Template: Mark an annotation as favorite
    Given I am reading the book <document_title>
    And I want to take an important note <text>
    When I mark the note as favorite
    Then I should see the note with the mark <favorite>

    Examples:
      |      document_title      | text                                |  favorite   |
      | Lean Software            | Tomar en cuenta estos principios    | True        |
      | Math Book                | Estudiar esto                       | True       |
      | Physics Book             | ""                                  | True        |
