# Created by thoma at 23/8/2023
@documents_setup
@documents_purge
Feature: Upload public articles
  As a teacher I want to be able to upload public articles to supplement reading on certain topics.

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

  Scenario Outline: Upload articles
    Given a pdf file <pdf_name>
    When I upload the article as <subject>
    Then the article must be on <subject_path>

    Examples:
      |     pdf_name        |subject  |  subject_path                                          |
      | mathArticle.pdf     | Math    | static/articles/resources/MathResources/*/mathArticle.pdf       |
      | physicsArticle.pdf  | Physics | static/articles/resources/PhysicsResources/*/physicsArticle.pdf |

  Scenario Outline: Serve file
    Given a pdf file <pdf_name>
    When I upload the article as <subject>
    Then the article is available through http/s

    Examples:
      |pdf_name           |  subject |
      |mathArticle.pdf    |  Math    |
      |physicsArticle.pdf |  Physics |

  @fake_data
  Scenario Outline: Avoid duplicate by hash collision
    Given a document A
    And a pdf file <filename>
    When a A hash check is performed on <filename>
    Then <collisions_number> collision/s were/was found

    Examples:
    |filename|collisions_number|
    |   A.pdf|  one            |
    |   B.pdf|  zero           |

  @fake_data
  Scenario: Scoring of an unrated document
    Given a document A
    Then document A's final score must be 0

  @fake_data
  Scenario Outline: Average book score
    Given a document A
    And someone scores document A a <score_a>
    When someone else scores document A a <score_b>
    Then document A's final score must be <book_score>
    Examples:
    | score_a | score_b | book_score|
    |  2      |   4     | 3         |
    |  1      |   3     | 2         |
    |  2      |   4     | 3         |

  @fake_data
  Scenario Outline: Individual scoring per book
    Given a document A
    And a document B
    And person scores document A a <a_score>
    And person scores document B a <b_score>
    Then document A's final score must be <final_a_score>
    Then document B's final score must be <final_b_score>
    Examples:
    | a_score | b_score | final_a_score | final_b_score |
    |  2      |   4     |  2            |  4            |
    |  1      |   3     |  1            |  3            |
    |  2      |   4     |  2            |  4            |