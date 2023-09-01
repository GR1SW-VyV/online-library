from behave import *
from annotations.models.note import Note
from annotations.models.user import User
from annotations.models.document import Document
from annotations.models.generalnote import GeneralNote

use_step_matcher("re")



@given('I am reading a document about "Lean Software Development"')
def step_impl(context):
    context.document = Document("Lean Software Development", 3)
    context.user = User(3)

@when('I add a note with the text "Tomar en cuenta estos principios" in the page 10')
def step_impl(context):
    context.note = Note(1, "Tomar en cuenta estos principios", 10, 3, 3)
    context.document.add_notePage(context.note)

@then("I should see the note in the notes section")
def step_impl(context):
    assert context.document.notePage_in_document(context.note)






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


