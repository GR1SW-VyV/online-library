from behave import *

use_step_matcher("re")


@given("I am reading a document (?P<name_document>.+)")
def step_impl(context, name_document):
    """
    :type context: behave.runner.Context
    :type name_document: str
    """
    raise NotImplementedError(u'STEP: Given I am reading a document <name_document>')


@when("I add a note with the text (?P<note_text>.+) of page (?P<number_page>.+)")
def step_impl(context, note_text, number_page):
    """
    :type context: behave.runner.Context
    :type note_text: str
    :type number_page: str
    """
    raise NotImplementedError(u'STEP: When I add a note with the text <note_text> of page <number_page>')


@then("I should see the note in the notes section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see the note in the notes section')


@given("I am seeing the document information about (?P<name_document>.+)")
def step_impl(context, name_document):
    """
    :type context: behave.runner.Context
    :type name_document: str
    """
    raise NotImplementedError(u'STEP: Given I am seeing the document information about <name_document>')


@when("I add an note with the text (?P<annotation_text>.+)")
def step_impl(context, annotation_text):
    """
    :type context: behave.runner.Context
    :type annotation_text: str
    """
    raise NotImplementedError(u'STEP: When I add an note with the text <annotation_text>')


@then("I should see the note with the information of the document")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see the note with the information of the document')


@when("I mark the note as favorite")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I mark the note as favorite')


@then("I should see the note with the mark")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see the note with the mark')