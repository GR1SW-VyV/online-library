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


  Scenario Outline: Serve file
    Given <local_path> on the disk
    And  <title>, <author>, <subject>
    When the article is uploaded
    Then it must auto generate a <unique_id>
    And the file is available at <subject_path> through http/s

    Examples:
      |local_path                                          | title                | author          | subject | unique_id   | subject_path                                           |
      |articles/test/resources/articles/mathArticle.pdf    | Arirmetica de Baldor | Aurelio Baldor | Math    | ArAuMath    | articles/resources/MathResources/mathArticle.pdf       |
      |articles/test/resources/articles/physicsArticle.pdf | Fisica Cuantica      | Max Planck     | Physics | FiMaPhysics | articles/resources/PhysicsResources/physicsArticle.pdf |


  Scenario Outline: Avoid duplicate files
    Given <file> from a <subject>
    When I upload another <upload-file> at the same <subject>
    Then if the file is the same send an error <message>

    Examples:
      |  file                                               |subject  |  upload-file                                           | message                              |
      |articles/test/resources/articles/mathArticle.pdf     | Math    |articles/resources/MathResources/mathArticle.pdf        |The file already exist                |
      |articles/test/resources/articles/physicsArticle.pdf  | Physics |articles/resources/PhysicsResources/physicsArticle.pdf  |The file already exist                |

  Scenario Outline: Suggest author for autocomplete
    Given the text "<text>"
    When lookup for an author
    Then it must return an <array> from authors
    Examples:
      | text | array                                                |
      | B    |["Baldor Aurelio", "Balaca Ricardo", "Berro Adolfo"]  |
      |Ba    |["Baldor Aurelio", "Balaca Ricardo"]                  |
      |Be    |["Berro Adolfo"]                                      |
