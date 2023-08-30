from behave import *
from annotations.models.notee import Note
from annotations.models.userr import User
from annotations.models.documen import Document

use_step_matcher("re")


@given("I am reading a document (?P<name_document>.+)")
def step_impl(context, name_document):
    context.document = Document


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


@given('I am reading the book "Cien años de soledad"')
def step_impl(context):
    context.document = Document(1, "Cien años de soledad")
    context.user = User(1)


@step("I want to take an important note")
def step_impl(context):
    context.note = Note(1, "Me parece muy importante la linea 23", 23, 1, 1)
    context.user.add_note(context.note)


@when("I mark the note as favorite")
def step_impl(context):
    nota = context.user.get_note_by_id(1)
    nota.set_importance()


@then("I should see the note with the mark")
def step_impl(context):
    note = context.user.get_note_by_id(1)
    assert note.is_important is True
