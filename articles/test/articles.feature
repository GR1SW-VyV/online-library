# Created by thoma at 23/8/2023
Feature: Upload public articles
  As a teacher I want to be able to upload public articles to supplement reading on certain topics.

  Scenario Outline: Upload articles
    Given <local_path> on the disk
    When I upload the article as <subject>
    Then the article must be on <subject_path>
    And <message> will be displayed

    Examples:
      |  local_path                                         |subject  |  subject_path                                               | message                              |
      |articles/test/resources/articles/mathArticle.pdf     | Math    |articles/resources/MathResources/mathArticle.pdf        |Successful upload to Math Resources   |
      |articles/test/resources/articles/physicsArticle.pdf  | Physics |articles/resources/PhysicsResources/physicsArticle.pdf  |Successful upload to Physics Resources|

