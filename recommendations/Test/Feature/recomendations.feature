# language: en

Feature: : Reading recommendations
    As a user, I want to be recommended readings based on the
    content of my collections to discover material of interest to me

  Scenario Outline: Recommendations based on a preferences
    Given users has no collections
    And send preferences <preference1> <preference2> <preference3>
    When the reader wants recommendations
    Then a set of <num_recomendations> most visited readings of <preference1> are recommended
    And a set of <num_recomendations> most visited readings of <preference2> are recommended
    And a set of <num_recomendations> most visited readings of <preference3> are recommended

    Examples:
    |preference1      |preference2   |preference3  |num_recomendations|
    |"programacion"   |"matematica"  |"lenguaje"   |4                 |


  Scenario Outline: Recommendations based on a collection
    Given users has collections
    And have this most common categories <category1> <category2> <category3>
    When the reader wants recommendations
    Then a set of <num_recomendations1> most visited readings of <categoria1> are recommended
    And a set of <num_recomendations2> most visited readings of <categoria2> are recommended
    And a set of <num_recomendations3> most visited readings of <categoria3> are recommended

    Examples:
    | category1      | category2    |category3  |num_recomendations1|num_recomendations2| num_recomendations3|
    |"programacion"  |"matematica"  |"lenguaje" |4                  |4                   |4                   |
    |"programacion"  |"matematica"  |" "        |4                  |4                   |0                   |
    |"programacion"  |" "           |"  "       |4                  |0                   |0                   |