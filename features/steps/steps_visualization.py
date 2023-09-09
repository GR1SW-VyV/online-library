from behave import *

use_step_matcher("re")


@given("I have the document (?P<document_title>.+) with the id (?P<document_id>.+)")
def step_impl(context, document_title, document_id):
    """
    :type context: behave.runner.Context
    :type document_title: str
    :type document_id: str
    """
    raise NotImplementedError(u'STEP: Given I have the document <document_title> with the id <document_id>')


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    raise NotImplementedError(u'STEP: * I am logged in with my username <username>')


@step("there are notes (?P<my_general_notes>.+) added by me on (?P<date>.+) date")
def step_impl(context, my_general_notes, date):
    """
    :type context: behave.runner.Context
    :type my_general_notes: str
    :type date: str
    """
    raise NotImplementedError(u'STEP: * there are notes <my_general_notes> added by me on <date> date')


@when("I want to read my notes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I want to read my notes')


@then("it should display my personal notes (?P<my_ordered_general_notes>.+) ordered by date")
def step_impl(context, my_ordered_general_notes):
    """
    :type context: behave.runner.Context
    :type my_ordered_general_notes: str
    """
    raise NotImplementedError(
        u'STEP: Then it should display my personal notes <my_ordered_general_notes> ordered by date')


@step("there are notes (?P<my_notes>.+) added by me in the page (?P<page_number>.+) on (?P<date>.+) date")
def step_impl(context, my_notes, page_number, date):
    """
    :type context: behave.runner.Context
    :type my_notes: str
    :type page_number: str
    :type date: str
    """
    raise NotImplementedError(
        u'STEP: * there are notes <my_notes> added by me in the page <page_number> on <date> date')


@when("I want to read my notes in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    raise NotImplementedError(u'STEP: When I want to read my notes in the page <page_number>')


@then("it should display my personal notes (?P<my_ordered_notes>.+) ordered by date and favorite")
def step_impl(context, my_ordered_notes):
    """
    :type context: behave.runner.Context
    :type my_ordered_notes: str
    """
    raise NotImplementedError(
        u'STEP: Then it should display my personal notes <my_ordered_notes> ordered by date and favorite')


@step("I am a (?P<user_type>.+) logged in with my username (?P<username>.+)")
def step_impl(context, user_type, username):
    """
    :type context: behave.runner.Context
    :type user_type: str
    :type username: str
    """
    raise NotImplementedError(u'STEP: * I am a <user_type> logged in with my username <username>')


@step("I have (?P<followers>.+) followers")
def step_impl(context, followers):
    """
    :type context: behave.runner.Context
    :type followers: str
    """
    raise NotImplementedError(u'STEP: * I have <followers> followers')


@step(
    "there are general notes (?P<general_notes>.+) added by other users on (?P<date>.+) date marked as (?P<is_favorite>.+) favorite")
def step_impl(context, general_notes, date, is_favorite):
    """
    :type context: behave.runner.Context
    :type general_notes: str
    :type date: str
    :type is_favorite: str
    """
    raise NotImplementedError(
        u'STEP: * there are general notes <general_notes> added by other users on <date> date marked as <is_favorite> favorite')


@when("I want to read the general notes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I want to read the general notes')


@then("it should display the general notes (?P<ordered_general_notes>.+) ordered by date and favorite")
def step_impl(context, ordered_general_notes):
    """
    :type context: behave.runner.Context
    :type ordered_general_notes: str
    """
    raise NotImplementedError(
        u'STEP: Then it should display the general notes <ordered_general_notes> ordered by date and favorite')


@step(
    "there are notes (?P<notes>.+) added by other users in the page (?P<page_number>.+) on (?P<date>.+) date marked as (?P<is_favorite>.+) favorite")
def step_impl(context, notes, page_number, date, is_favorite):
    """
    :type context: behave.runner.Context
    :type notes: str
    :type page_number: str
    :type date: str
    :type is_favorite: str
    """
    raise NotImplementedError(
        u'STEP: * there are notes <notes> added by other users in the page <page_number> on <date> date marked as <is_favorite> favorite')


@when("I want to read the notes in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    raise NotImplementedError(u'STEP: When I want to read the notes in the page <page_number>')


@then("it should display the notes (?P<ordered_notes>.+) ordered by date and favorite")
def step_impl(context, ordered_notes):
    """
    :type context: behave.runner.Context
    :type ordered_notes: str
    """
    raise NotImplementedError(u'STEP: Then it should display the notes <ordered_notes> ordered by date and favorite')
