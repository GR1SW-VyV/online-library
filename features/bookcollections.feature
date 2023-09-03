# Created by Cebastian at 22/8/2023
Feature: Generate a Book Collection
  As reader I want to create private or public book collections to be able to share my tastes and interests.
    Scenario: Creation of a book collection
    Scenario Outline:
      Given the collection's name: <name>, description: <description> type of privacy: <type_privacy>
      And the book <book_name> with <book_score> points
      When the user creates the collection
      Then the collection will be created with the given name, description and type of privacy
      And will contain the given book
      And will have <collection_score> points

      Examples:
      |name              |description                                 |type_privacy|book_name                       |book_score|
      |Math Books        |This my Math Books collection               |True        |"Baldor's Algebra"              |10        |
      |Chemistry Books   |My personal Chemistry Books collection      |False       |"The name of the wind"          |20        |
      |Personal Books    |All the books I love                        |True        |"The way to the self-discovery" |30        |

  Scenario: Calculating the value of a collection
    Scenario Outline:
      Given the collection with the books: <book_1> and <book_2>
      And their respectives points: <book_score_1>, <book_score_2>
      And the user want to add the book <book_3> with <book_score_3>
      When the user adds the book <book_3>
      Then the collection score will be <collection_points> representing average points of all books
      Examples:
      |book_1      |book_2           |book_score_1|book_score_2|book_3              |book_score_3|collection_points|
      |"The Hobbit"|"Harry Potter"   |	8	       |9	        |"Lord of the Rings"|10	         |9                |
      |"1984"      |"Brave new world"|	7	       |8	        |"Fahrenheit 451"   |9	         |8                |
      |"To Kill a Mockingbird"|"The Great Gatsby"|9|8      |"Pride and Prejudice" |9       |8.67             |
