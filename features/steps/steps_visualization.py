from behave import *
from expects import *


use_step_matcher("re")


@given("I have the book (?P<book_id>.+)")
def step_impl(context, book_id):
    """
    :type context: behave.runner.Context
    :type book_id: str
    """
    context.book_id = book_id


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.username = username


@when("I am reading the details of the book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.general_notes = ""
    context.my_general_notes = ""

@then("it should display my personal general notes (?P<my_general_notes>.+)")
def step_impl(context, my_general_notes):
    """
    :type context: behave.runner.Context
    :type my_general_notes: str
    """
    expect(context.my_general_notes).to(equal(my_general_notes))


@step("the general notes (?P<general_notes>.+) from other users ordered by their number of followers\.")
def step_impl(context, general_notes):
    """
    :type context: behave.runner.Context
    :type general_notes: str
    """
    expect(context.general_notes).to(equal(general_notes))


@when("I am reading the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    context.my_notes = ""
    context.notes = ""


@then("it should display my personal notes (?P<my_notes>.+)")
def step_impl(context, my_notes):
    """
    :type context: behave.runner.Context
    :type my_notes: str
    """
    expect(context.my_notes).to(equal(my_notes))


@step("the notes (?P<notes>.+) from other users ordered by their number of followers\.")
def step_impl(context, notes):
    """
    :type context: behave.runner.Context
    :type notes: str
    """
    expect(context.notes).to(equal(notes))
