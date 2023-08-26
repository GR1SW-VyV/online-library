from behave import *

use_step_matcher("re")


@given("the book Clean Code")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the book Clean Code')


@when("I am reviewing the details of the book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I am reviewing the details of the book')


@then("it should display the following reviews:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then it should display the following reviews:
    | Marcela Tapia | 21 - 03 - 2023 | A must - read for programmers! |
    | Bryan Montalvo | 07-04-2023 | Great insights and examples.|
    | Adamaris Diaz | 14-05-2023 | Practical advice for coding.|
    | Mateo Gavilanez | 15-06-2023 | Well-organized and helpful.|
    | Cristopher Perez | 04-07-2023 | Changed how I write code.| ')


@when("I am reading the page {page_number}")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I am reading the page <page_number>')


@when("I am reading the page <page_number>")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I am reading the page <page_number>')


@then("it should display the following notes:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then it should display the following notes:
                              | user | page_number | date | is_important | content |
                              | Marcela
    Tapia | 1 | 21 - 03 - 2023 | True | Important
    introduction
    points. |
    | Bryan
    Montalvo | 1 | 07 - 04 - 2023 | False | Interesting
    examples
    here. |
    | Adamaris
    Diaz | 1 | 14 - 05 - 2023 | True | Don\'t forget these concepts.   |
                                           | Mateo
    Gavilanez | 1 | 15 - 06 - 2023 | False | Helpful
    insights
    on
    page
    1. |
    | Cristopher
    Perez | 1 | 04 - 07 - 2023 | False | Noted
    down
    a
    few
    tips. |
    | Marcela
    Tapia | 2 | 21 - 03 - 2023 | False | Explained
    well
    on
    page
    2. |
    | Bryan
    Montalvo | 2 | 07 - 04 - 2023 | True | Important
    details
    here. |
    | Adamaris
    Diaz | 2 | 14 - 05 - 2023 | False | Skipped
    this
    part. |
    | Mateo
    Gavilanez | 2 | 15 - 06 - 2023 | False | Not
    relevant
    for me. |
        | Cristopher Perez | 2 | 04 - 07 - 2023 | True | Remember for future projects.| ')