from behave import *
from annotations.models.note import Note
from annotations.models.user import User
from annotations.models.document import Document
from annotations.models.generalnote import GeneralNote

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


@given('I am seeing the document information about "Ensayo sobre la ceguera"')
def step_impl(context):
    context.document = Document("Ensayo sobre la ceguera",2)
    context.user = User(2)



@when('I add an note with the text "Que interesante libro"')
def step_impl(context):
    context.generalNote = GeneralNote("Que interesante libro",2,2)
    context.document.add_generalNote(context.generalNote)

@then("I should see the note with the information of the document")
def step_impl(context):
    assert context.document.note_in_document(context.generalNote)


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


