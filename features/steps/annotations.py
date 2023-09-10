from behave import *

use_step_matcher("re")


@given("I am reading a document (?P<document_title>.+)")
def step_impl(context, document_title):
    raise NotImplementedError(u'STEP: Given I am reading a document <document_title>')


@when("I add a note with the text (?P<text>.+) in the page (?P<page_number>.+)")
def step_impl(context, text, page_number):
    raise NotImplementedError(u'STEP: When I add a note with the text <text> in the page <page_number>')


@then("I should see the note in the notes section of the page (?P<page_number>.+)")
def step_impl(context, page_number):
    raise NotImplementedError(u'STEP: Then I should see the note in the notes section of the page <page_number>')


@given("I am seeing the document information about a document (?P<document_title>.+)")
def step_impl(context, document_title):
    raise NotImplementedError(u'STEP: Given I am seeing the document information about a document <document_title>')


@when("I add an note with the text (?P<text>.+)")
def step_impl(context, text):
    raise NotImplementedError(u'STEP: When I add an note with the text <text>')


@then("I should see the note with the information of the document (?P<document_title>.+)")
def step_impl(context, document_title):
    raise NotImplementedError(u'STEP: Then I should see the note with the information of the document <document_title>')


@given("I am reading the book (?P<document_title>.+)")
def step_impl(context, document_title):
    raise NotImplementedError(u'STEP: Given I am reading the book <document_title>')


@step("I want to take an important note (?P<text>.+)")
def step_impl(context, text):
    raise NotImplementedError(u'STEP: And I want to take an important note <text>')


@when("I mark the note as favorite (?P<favorite>.+)")
def step_impl(context, favorite):
    raise NotImplementedError(u'STEP: When I mark the note as favorite <favorite>')


@then("I should see the note with the mark (?P<favorite>.+)")
def step_impl(context, favorite):
    raise NotImplementedError(u'STEP: Then I should see the note with the mark <favorite>')