from behave import *
from faker import Faker
from annotations.testmodels.note import Note as TestNote
from annotations.testmodels.user import User as TestUser
from annotations.testmodels.document import Document as TestDocument
from annotations.testmodels.generalnote import GeneralNote as TestGneralNote

from social.models import User
from articles.models import Document
from annotations.models import PageNote, PageNoteDAO

use_step_matcher("re")


@given('I am reading a document about "Lean Software Development"')
def step_impl(context):
    context.document = TestDocument("Lean Software Development", 3)
    context.user = TestUser(3)


@when('I add a note with the text "Tomar en cuenta estos principios" in the page 10')
def step_impl(context):
    context.note = TestNote(1, "Tomar en cuenta estos principios", 10, 3, 3)
    context.document.add_notePage(context.note)


@then("I should see the note in the notes section")
def step_impl(context):
    assert context.document.notePage_in_document(context.note)


@given('I am seeing the document information about "Ensayo sobre la ceguera"')
def step_impl(context):
    context.document = TestDocument("Ensayo sobre la ceguera", 2)
    context.user = TestUser(2)


@when('I add an note with the text "Que interesante libro"')
def step_impl(context):
    context.generalNote = TestGneralNote("Que interesante libro", 2, 2)
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
        password=faker.password()
    )


@step("I want to take an important note")
def step_impl(context):
    context.note = PageNote.objects.create(
        content="Me parece muy importante la línea 23",
        page=23,
        user=context.user,
        document=context.document,
    )


@when("I mark the note as favorite")
def step_impl(context):
    PageNoteDAO.mark_note_as_favorite(context.note.id)


@then("I should see the note with the mark")
def step_impl(context):
    note = PageNoteDAO.get_note_by_id(context.note.id)
    assert note.is_favorite is True
