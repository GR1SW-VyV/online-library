# Created by leoasitimbaya at 24/8/2023
Feature: Write notes

  As a reader I want to make notes in a document to synthesize and facilitate my learning.

  Scenario Template: Take notes of a page of a document
    Given I am reading a document <name_document>
    When I add a note with the text <note_text> of page <number_page>
    Then I should see the note in the notes section
    Examples:
      | name_document            | note_text                      | number_page |
      | "sample_document.pdf"    | "This is a test annotation"    | 1           |
      | "chapter1.docx"          | "Important note here"          | 3           |
      | "research_paper.html"    | "Review this section later"    | 5           |
      | "ebook.epub"             | "Highlight this paragraph"     | 2           |

  Scenario Template: Take notes of a document
    Given I am seeing the document information about <name_document>
    When I add an note with the text <annotation_text>
    Then I should see the note with the information of the document


    Examples:
      | name_document            | annotation_text                |
      | "sample_document.pdf"    | "This is a test annotation"    |
      | "chapter1.docx"          | "Important note here"          |
      | "research_paper.html"    | "Review this section later"    |
      | "ebook.epub"             | "Highlight this paragraph"     |

  Scenario Template: Mark an annotation as favorite

    Given I am reading a document <name_document>
    When I mark the note as favorite
    Then I should see the note with the mark
    Examples:
      | name_document            | annotation_text                | favorite_boolean |
      | "sample_document.pdf"    | "This is a test annotation"    | true             |
      | "chapter1.docx"          | "Important note here"          | false            |
      | "research_paper.html"    | "Review this section later"    | true             |
      | "ebook.epub"             | "Highlight this paragraph"     | false            |