from behave import *

use_step_matcher("re")


@given("I have the document (?P<document_title>.+) with the id (?P<document_id>.+)")
def step_impl(context, document_title, document_id):
    raise NotImplementedError(u'STEP: Given I have the document <document_title> with the id <document_id>')


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    raise NotImplementedError(u'STEP: * I am logged in with my username <username>')


@step("there are notes (?P<my_general_notes>.+) added by me on (?P<date>.+) date")
def step_impl(context, my_general_notes, date):
    raise NotImplementedError(u'STEP: * there are notes <my_general_notes> added by me on <date> date')


@when("I want to read my notes")
def step_impl(context):
    raise NotImplementedError(u'STEP: When I want to read my notes')


@then("it should display my personal notes (?P<my_ordered_general_notes>.+) ordered by date")
def step_impl(context, my_ordered_general_notes):
    raise NotImplementedError(
        u'STEP: Then it should display my personal notes <my_ordered_general_notes> ordered by date')


@step("there are notes (?P<my_notes>.+) added by me in the page (?P<page_number>.+) on (?P<date>.+) date")
def step_impl(context, my_notes, page_number, date):
    raise NotImplementedError(
        u'STEP: * there are notes <my_notes> added by me in the page <page_number> on <date> date')


@when("I want to read my notes in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    raise NotImplementedError(u'STEP: When I want to read my notes in the page <page_number>')


@then("it should display my personal notes (?P<my_ordered_notes>.+) ordered by date and favorite")
def step_impl(context, my_ordered_notes):
    raise NotImplementedError(
        u'STEP: Then it should display my personal notes <my_ordered_notes> ordered by date and favorite')


@step("I have (?P<followers>.+) followers")
def step_impl(context, followers):
    raise NotImplementedError(u'STEP: * I have <followers> followers')


@step("I am (?P<user_type>.+) user")
def step_impl(context, user_type):
    raise NotImplementedError(u'STEP: * I am <user_type> user')


@step(
    "there are general notes (?P<general_notes>.+) added by other users on (?P<date>.+) date marked as (?P<is_favorite>.+) favorite")
def step_impl(context, general_notes, date, is_favorite):
    raise NotImplementedError(
        u'STEP: * there are general notes <general_notes> added by other users on <date> date marked as <is_favorite> favorite')


@when("I want to read the general notes")
def step_impl(context):
    raise NotImplementedError(u'STEP: When I want to read the general notes')


@then("it should display the general notes (?P<ordered_general_notes>.+) ordered by date and favorite")
def step_impl(context, ordered_general_notes):
    raise NotImplementedError(
        u'STEP: Then it should display the general notes <ordered_general_notes> ordered by date and favorite')


@step(
    "there are notes (?P<notes>.+) added by other users in the page (?P<page_number>.+) on (?P<date>.+) date marked as (?P<is_favorite>.+) favorite")
def step_impl(context, notes, page_number, date, is_favorite):
    raise NotImplementedError(
        u'STEP: * there are notes <notes> added by other users in the page <page_number> on <date> date marked as <is_favorite> favorite')


@when("I want to read the notes in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    raise NotImplementedError(u'STEP: When I want to read the notes in the page <page_number>')


@then("it should display the notes (?P<ordered_notes>.+) ordered by date and favorite")
def step_impl(context, ordered_notes):
    raise NotImplementedError(u'STEP: Then it should display the notes <ordered_notes> ordered by date and favorite')