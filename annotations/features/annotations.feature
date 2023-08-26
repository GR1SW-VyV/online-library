# Created by leoasitimbaya at 24/8/2023
Feature: Write annotations

  As a reader I want to make notes in a document to synthesize and facilitate my learning.

  Scenario: Take notes on a document by page
    Given I am reading a document <name_document>
    When I add an annotation with the text <annotation_text> on page <number_page>
    Then I should see the annotation on page <number_page>

  Scenario: Take notes on a document
    Given I am reading a document <name_document>
    When I add an annotation with the text <annotation_text>
    Then I should see the annotation

  Scenario: Mark an annotation as favorite
    Given I am reading a document <name_document>
    When I add an annotation with the text <annotation_text>
    And I mark the annotation as favorite
    Then I should see the annotation as favorite

