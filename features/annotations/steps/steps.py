from behave import *
from faker import Faker
from annotations.testmodels.note import Note
from annotations.testmodels.user import User
from annotations.testmodels.document import Document
from annotations.testmodels.generalnote import GeneralNote

from annotations.models import Note, NoteDAO
from social.models import User
from articles.models import Document

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
    context.document = Document("Ensayo sobre la ceguera", 2)
    context.user = User(2)


@when('I add an note with the text "Que interesante libro"')
def step_impl(context):
    context.generalNote = GeneralNote("Que interesante libro", 2, 2)
    context.document.add_generalNote(context.generalNote)


@then("I should see the note with the information of the document")
def step_impl(context):
    assert context.document.note_in_document(context.generalNote)


@given('I am reading the book "Cien años de soledad"')
def step_impl(context):

    context.document = Document.objects.create(
        title="Cien años de soledad"
    )

    faker = Faker()
    context.user = User.objects.create(
        username=faker.user_name(),
    )


@step("I want to take an important note")
def step_impl(context):
    context.note = Note.objects.create(
        content="Me parece muy importante la línea 23",
        page=23,
        user=context.user,
        document=context.document,
    )


@when("I mark the note as favorite")
def step_impl(context):
    NoteDAO.mark_note_as_favorite(context.note.id)


@then("I should see the note with the mark")
def step_impl(context):
    note = NoteDAO.get_note_by_id(context.note.id)
    assert note.is_favorite is True
