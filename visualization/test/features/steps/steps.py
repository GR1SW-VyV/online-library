from behave import *

use_step_matcher("re")


@given("I have the book (?P<book>.+) with the id (?P<book_id>.+)")
def step_impl(context, book, book_id):
    """
    :type context: behave.runner.Context
    :type book: str
    :type book_id: str
    """
    raise NotImplementedError(u'STEP: Given I have the book <book> with the id <book_id>')


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    raise NotImplementedError(u'STEP: And I am logged in with my username <username>')


@when("I am reading the details of the book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I am reading the details of the book')


@then("it should display my personal general annotations (?P<my_general_annotations>.+)")
def step_impl(context, my_general_annotations):
    """
    :type context: behave.runner.Context
    :type my_general_annotations: str
    """
    raise NotImplementedError(u'STEP: Then it should display my personal general annotations <my_general_annotations>')


@step("the general annotattions (?P<general_annotations>.+) from other users ordered by their number of followers\.")
def step_impl(context, general_annotations):
    """
    :type context: behave.runner.Context
    :type general_annotations: str
    """
    raise NotImplementedError(
        u'STEP: And the general annotattions <general_annotations> from other users ordered by their number of followers.')


@when("I am reading the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    raise NotImplementedError(u'STEP: When I am reading the page <page_number>')


@then("it should display my personal annotations (?P<my_annotations>.+)")
def step_impl(context, my_annotations):
    """
    :type context: behave.runner.Context
    :type my_annotations: str
    """
    raise NotImplementedError(u'STEP: Then it should display my personal annotations <my_annotations>')


@step("the annotations (?P<annotations>.+) from other users ordered by their number of followers\.")
def step_impl(context, annotations):
    """
    :type context: behave.runner.Context
    :type annotations: str
    """
    raise NotImplementedError(
        u'STEP: And the annotations <annotations> from other users ordered by their number of followers.')