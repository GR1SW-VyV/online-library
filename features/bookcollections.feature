# Created by Cebastian at 22/8/2023
Feature: Generate a Book Collection
  As reader I want to create private or public book collections to be able to share my tastes and interests.

  Scenario: Adding a book to collection
    Scenario Outline:
      Given a collection's name: <name_collection> and the book: <name_book>
      When the user add the book to collection
      Then the book will be displayed into the collection

      Examples:
      |name_collection|name_book            |
      |Math Books     |Baldor - Mathematics |
      |Chemistry Books|Chemistry for dummies|
      |Personal Books |The name of the wind |

  Scenario: Creation of a book collection
    Scenario Outline:
      Given the collection's name: <name>, description: <description> and type of privacy: <type_privacy>
      When the user create the collection
      Then the collection will be created with the information given

      Examples:
      |name              |description                                 |type_privacy|
      |Math Books        |This my Math Books collection               |public      |
      |Chemistry Books   |My personal Chemistry Books collection      |private     |
      |Personal Books    |All the books I love                        |public      |
