from behave import *
from faker import Faker

from annotations.models import PageNote, PageNoteDAO
from articles.models import Document
from social.models import User
from visualization.models import GeneralNote, GeneralNoteDAO

use_step_matcher("re")


@given("I am reading a document (?P<document_title>.+)")
def step_impl(context, document_title):
    new_document = Document.objects.create(title=document_title)
    new_document.save()
    context.document = new_document

    faker = Faker()
    context.user = User.objects.create(
        username=faker.name(),
        email=faker.email(),
        password=faker.password()
    )


@when("I add a note with the text (?P<text>.+) in the page (?P<page_number>.+)")
def step_impl(context, text, page_number):
    document = Document.objects.get(uid=context.document.uid)

    context.note = PageNote.objects.create(content=text, page=page_number, user_id=context.user.id,
                                           document_id=document.uid)


@then("I should see the note in the notes section of the page (?P<page_number>.+)")
def step_impl(context, page_number):
    notes = PageNoteDAO.get_notes_by_page(context.user.id, context.document.uid, page_number)
    assert context.note in notes


@given("I am seeing the document information about a document (?P<document_title>.+)")
def step_impl(context, document_title):
    new_document = Document.objects.create(title=document_title)
    new_document.save()
    context.document = new_document

    faker = Faker()
    context.user = User.objects.create(
        username=faker.name(),
        email=faker.email(),
        password=faker.password()
    )

@when("I add an note with the text (?P<text>.+)")
def step_impl(context, text):
    print("Hola mundo " + text)
    document = Document.objects.get(uid=context.document.uid)
    context.generalNote = GeneralNote.objects.create(content=text, user_id=context.user.id, document_id=document.uid)

@then("I should see the note with the information of the document (?P<document_title>.+)")
def step_impl(context, document_title):
    notes = GeneralNoteDAO.get_general_notes(context.user.id, context.document.uid)
    assert context.generalNote in notes

@given("I am reading the book (?P<document_title>.+)")
def step_impl(context, document_title):
    new_document = Document.objects.create(title=document_title)
    new_document.save()
    context.document = new_document

    faker = Faker()
    context.user = User.objects.create(
        username=faker.name(),
        email=faker.email(),
        password=faker.password()
    )


@step("I want to take an important note (?P<text>.+)")
def step_impl(context, text):
    document = Document.objects.get(uid=context.document.uid)

    context.note = PageNote.objects.create(content=text,
                                           page=1,
                                           user_id=context.user.id,
                                           document_id=document.uid)


@when("I mark the note as favorite")
def step_impl(context):
    note = PageNote.objects.get(id=context.note.id)
    PageNoteDAO.mark_note_as_favorite(note.id)


@then("I should see the note with the mark (?P<favorite>.+)")
def step_impl(context, favorite):
    note = PageNote.objects.get(id=context.note.id)
    assert note.is_favorite
