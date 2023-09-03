# Created by thoma at 23/8/2023
Feature: Upload public articles
  As a teacher I want to be able to upload public articles to supplement reading on certain topics.

  Scenario Outline: Upload articles
    Given <local_path> on the disk
    When I upload the article as <subject>
    Then the article must be on <subject_path>

    Examples:
      |  local_path                                         |subject  |  subject_path |
      |articles/test/resources/articles/mathArticle.pdf     | Math    |articles/resources/MathResources/mathArticle.pdf|
      |articles/test/resources/articles/physicsArticle.pdf  | Physics |articles/resources/PhysicsResources/physicsArticle.pdf |


  Scenario Outline: Serve file
    Given <local_path> on the disk
    And  <title>, <author>, <subject>
    When the article is uploaded
    Then the file is available at <subject_path> through http/s

    Examples:
      |local_path                                          | title                | author          | subject    | subject_path                                           |
      |articles/test/resources/articles/mathArticle.pdf    | Arirmetica de Baldor | Aurelio Baldor | Math    | articles/resources/MathResources/mathArticle.pdf       |
      |articles/test/resources/articles/physicsArticle.pdf | Fisica Cuantica      | Max Planck     | Physics | articles/resources/PhysicsResources/physicsArticle.pdf |


  Scenario Outline: Avoid duplicate by hash collision
    Given  <title>, <author>, <subject>
    And <a_local_path> on the disk has been uploaded
    And <local_path> on the disk
    When a hash check is performed
    Then <warnings> collision is found
    And <warnings> colliding file is shown

    Examples:
      | a_local_path                                           | local_path                                         | title                | author         | subject | warnings |
      |    articles/test/resources/articles/physicsArticle.pdf    |articles/test/resources/articles/mathArticle.pdf    | Arirmetica de Baldor | Aurelio Baldor | Math    | no       |
      |    articles/test/resources/articles/physicsArticle.pdf |articles/test/resources/articles/physicsArticle.pdf | Fisica Cuantica      | Max Planck     | Physics | a        |

  Scenario Outline: Suggest author for autocomplete
    Given the text "<author_prefix>"
    And a default repertoire of Authors
    When lookup for an author
    Then it must return <array> as potential authors
    Examples:
      | author_prefix | array                                                |
      | B    |["Baldor Aurelio", "Balaca Ricardo", "Berro Adolfo"]  |
      | Ba    |["Baldor Aurelio", "Balaca Ricardo"]                  |
      | Be    |["Berro Adolfo"]                                      |
