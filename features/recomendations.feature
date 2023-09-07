# language: en

Feature: : Reading recommendations
    As a user, I want to be recommended readings based on the
    content of my collections to discover material of interest to me

  Scenario Outline: Recommendations based on a preferences
    Given users has no collections
    And send preferences <preference1> <preference2> <preference3>
    When the reader wants recommendations
    Then a set of <num_recommendations> most visited readings are recommended

    Examples:
    |preference1      |preference2   |preference3  |num_recommendations|
    |"programacion"   |"matematica"  |"lenguaje"   |12                |
    |"programacion"   |""            |""           |4                 |
    |"programacion"   |"matematica"  |""           |8                 |


  Scenario Outline: Recommendations based on a collection
    Given users has collections
    And have this most common categories <category1> <category2> <category3>
    When the reader wants recommendations
    Then a set of <num_recommendations> most visited readings are recommended based on their collections

    Examples:
    | category1      | category2    |category3  |num_recommendations|
    |"programacion"  |"matematica"  |"lenguaje" |12                 |
    |"programacion"  |"matematica"  |""         |8                  |
    |"programacion"  |""            |""         |4                  |