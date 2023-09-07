from behave import *
from expects import *
from faker import Faker

from articles.models import Document
from social.models import User

use_step_matcher("re")


@given("I have the document (?P<document_title>.+) with the id (?P<document_id>.+)")
def step_impl(context, document_title, document_id):
    """
    :type context: behave.runner.Context
    :type document_title: str
    :type document_id: str
    """
    pass


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.user = User.objects.create_reader_user(username=username, password=Faker().password())


@step("there are notes added by me and other users")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I want to compare my notes with those of other users")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("it should display my personal general notes (?P<my_general_notes>.+) ordered")
def step_impl(context, my_general_notes):
    """
    :type context: behave.runner.Context
    :type my_general_notes: str
    """
    expect(context.my_general_notes).to(equal(my_general_notes))


@step("the general notes (?P<general_notes>.+) from other users ordered\.")
def step_impl(context, general_notes):
    """
    :type context: behave.runner.Context
    :type general_notes: str
    """
    pass


@step("there are notes added by me and other users in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    pass


@when("I want to compare my notes with those of other users in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    pass


@then("it should display my personal notes (?P<my_notes>.+) ordered")
def step_impl(context, my_notes):
    """
    :type context: behave.runner.Context
    :type my_notes: str
    """
    expect(context.my_notes).to(equal(my_notes))


@step("the notes (?P<notes>.+) from other users ordered\.")
def step_impl(context, notes):
    """
    :type context: behave.runner.Context
    :type notes: str
    """
    expect(context.notes).to(equal(notes))