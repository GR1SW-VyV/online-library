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


  Scenario Outline: Generate unique ID
    Given <local_path> on the disk
    And  <title>, <autor>, <subject>
    When the article is uploaded
    Then it must auto generate a <unique_id>
    And the <unique_id> index with the <subject_path>

    Examples:
      |local_path                                          | title                | autor          | subject | unique_id   | subject_path                                           |
      |articles/test/resources/articles/mathArticle.pdf    | Arirmetica de Baldor | Aurelio Baldor | Math    | ArAuMath    | articles/resources/MathResources/mathArticle.pdf       |
      |articles/test/resources/articles/physicsArticle.pdf | Fisica Cuantica      | Max Planck     | Physics | FiMaPhysics | articles/resources/PhysicsResources/physicsArticle.pdf |
