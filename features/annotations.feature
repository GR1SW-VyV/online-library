# Created by leoasitimbaya at 24/8/2023
Feature: Write notes

  As a reader I want to make notes in a document to synthesize and facilitate my learning.

  Scenario Template: Take notes of a page of a document
    Given I am reading a document <document_title>
    When I add a note with the text <text> in the page <page_number>
    Then I should see the note in the notes section of the page <page_number_with_note>

    Examples:
      |      document_title      | text                                |  page_number | page_number_with_note |
      | Lean Software            | Tomar en cuenta estos principios    | 1            | 1                     |
      | Math Book                | Estudiar esto                       | 0            | 0                     |
      | Physics Book             |                                     | 1000         | 1000                  |

  Scenario: Take notes of a document
    Given I am seeing the document information about "Ensayo sobre la ceguera"
    When I add an note with the text "Que interesante libro"
    Then I should see the note with the information of the document



  Scenario: Mark an annotation as favorite
    Given I am reading the book "Cien años de soledad"
    And I want to take an important note
    When I mark the note as favorite
    Then I should see the note with the mark
