# Created by Cebastian at 22/8/2023
Feature: Generate a Book Collection
  As reader I want to create private or public book collections to be able to share my tastes and interests.
    Scenario: Creation of a book collection
    Scenario Outline:
      Given the collection's name: <name>, a description and type of privacy: <is_private>
      And the book <book_name> with <book_score> points
      When the user creates the collection
      Then the collection will be created with the given name, description and type of privacy
      And will contain the given book
      And will have <book_score> points

      Examples:
      |name              |is_private|book_name                       |book_score|
      |Math Books        |True        |"Baldor's Algebra"              |10        |
      |Chemistry Books   |False       |"The name of the wind"          |20        |
      |Personal Books    |True        |"The way to the self-discovery" |30        |

  Scenario: Calculating the value of a collection
    Scenario Outline:
      Given the collection with two books
      And their respective points: <book_score_1>, <book_score_2>
      And the user want to add a new book with <book_score_3> points
      When the user adds the book
      Then the collection score will be <collection_points> representing average points of all books
      Examples:
      |book_score_1|book_score_2|book_score_3|collection_points|
      |	8	       |9	        |10	         |9                |
      |	7	       |8	        |9	         |8                |
      |9           |8           |9           |8.67             |
