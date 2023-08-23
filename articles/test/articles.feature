# Created by thoma at 23/8/2023
Feature: Upload public articles
  As a teacher I want to be able to upload public articles to supplement reading on certain topics.

  Scenario Outline: Upload articles
    Given <local path> on the disk
    When I upload the article as <subject>
    Then the article must be on <subject path>
    And <message> will be displayed

    Examples:
      |  local path                  |subject    |  subject path                       | message                                |
      |"articles/resources/articles" | "Math"    |"articles/resources/MathResources"   |"Successful upload to Math Resources"   |
      |"articles/resources/articles" | "Physics" |"articles/resources/PhysicsResources"|"Successful upload to Physics Resources"|


