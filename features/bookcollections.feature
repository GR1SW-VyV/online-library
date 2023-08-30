# Created by Cebastian at 22/8/2023
Feature: Generate a Book Collection
  As reader I want to create private or public book collections to be able to share my tastes and interests.

  Scenario: Creation of a book collection
    Scenario Outline:
      Given the collection's name: <name>, description: <description> type of privacy: <type_privacy>
      And as optional a <book_name>
      When the user create the collection
      Then the collection will be created with the name, description and type of privacy given
      And with the book if it was given

      Examples:
      |name              |description                                 |type_privacy|book_name  |
      |Math Books        |This my Math Books collection               |True        |"Baldor's Algebra"|
      |Chemistry Books   |My personal Chemistry Books collection      |False       |null              |
      |Personal Books    |All the books I love                        |True        |"The way to the self-discovery"
