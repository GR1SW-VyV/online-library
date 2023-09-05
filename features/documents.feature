# Created by thoma at 23/8/2023
Feature: Upload public articles
  As a teacher I want to be able to upload public articles to supplement reading on certain topics.

  Scenario Outline: Upload articles
    Given <local_path> on the disk
    When I upload the article as <subject>
    Then the article must be on <subject_path>

    Examples:
      |  local_path                                         |subject  |  subject_path |
      |features/resources/articles/mathArticle.pdf     | Math    |articles/resources/MathResources/mathArticle.pdf|
      |features/resources/articles/physicsArticle.pdf  | Physics |articles/resources/PhysicsResources/physicsArticle.pdf |


  Scenario Outline: Serve file
    Given <local_path> on the disk
    And  <title>, <author>, <subject>
    When the article is uploaded
    Then the file is available at <subject_path> through http/s

    Examples:
      |local_path                                          | title                | author          | subject    | subject_path                                           |
      |features/resources/articles/mathArticle.pdf    | Arirmetica de Baldor | Aurelio Baldor | Math    | articles/resources/MathResources/mathArticle.pdf       |
      |features/resources/articles/physicsArticle.pdf | Fisica Cuantica      | Max Planck     | Physics | articles/resources/PhysicsResources/physicsArticle.pdf |


  Scenario Outline: Avoid duplicate by hash collision
    Given  <title>, <author>, <subject>
    And <a_local_path> on the disk has been uploaded
    And <local_path> on the disk
    When a hash check is performed
    Then <warnings> collision is found

    Examples:
      | a_local_path                                           | local_path                                         | title                | author         | subject | warnings |
      |    features/resources/articles/physicsArticle.pdf    |features/resources/articles/mathArticle.pdf    | Arirmetica de Baldor | Aurelio Baldor | Math    | no       |
      |    features/resources/articles/physicsArticle.pdf |features/resources/articles/physicsArticle.pdf | Fisica Cuantica      | Max Planck     | Physics | a        |

  Scenario Outline: Suggest author for autocomplete
    Given the text "<author_prefix>"
    And a default repertoire of Authors
    When lookup for an author
    Then it must return <array> as potential authors
    Examples:
      | author_prefix | array                                                |
      | B             |["Baldor Aurelio", "Balaca Ricardo", "Berro Adolfo"]  |
      | Ba            |["Baldor Aurelio", "Balaca Ricardo"]                  |
      | Be            |["Berro Adolfo"]                                      |

  Scenario: Scoring of an unrated document
    Given  title, author, Math
    And features/resources/articles/physicsArticle.pdf on the disk has been uploaded
    Then the final score must be 0

  Scenario Outline: Scoring
    Given  title, author, Math
    And features/resources/articles/physicsArticle.pdf on the disk has been uploaded
    When <user_a> scores the document a <score_a>
    And <user_b> scores the document a <score_b>
    Then the final score must be <final_score>
    Examples:
    | user_a  | score_a | user_b  | score_b | final_score|
    |  1      |  2      |  3      |   4     | 3.0        |
    |  1      |  1      |  3      |   3     | 2.0        |
    |  1      |  2      |  1      |   4     | 4.0        |
    |  2      |  2      |  1      |   -1    | 0.5        |

  Scenario Outline: Individual scoring per book
    Given  title, author, Math
    And features/resources/articles/physicsArticle.pdf on the disk has been uploaded
    And 1 scores the document a <score_a>
    And features/resources/articles/physicsArticle.pdf on the disk has been uploaded
    When 1 scores the document a <score_b>
    Then  the final score must be <document_b_score3>
    Examples:
    | score_a | score_b | document_b_score3|
    |  2      |   4     | 4        |
    |  1      |   3     | 3        |
    |  2      |   4     | 4        |
    |  2      |   -1    | -1        |