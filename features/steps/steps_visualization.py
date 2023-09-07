from behave import *
from expects import *
from faker import Faker

from articles.models import Document
from social.models import User
from visualization.models import GeneralNote, PageNote, GeneralNoteDAO, PageNoteDAO
from datetime import datetime

use_step_matcher("re")


@given("I have the document (?P<document_title>.+) with the id (?P<document_id>.+)")
def step_impl(context, document_title, document_id):
    """
    :type context: behave.runner.Context
    :type document_title: str
    :type document_id: str
    """
    context.document = Document.objects.create()
    context.document.id = document_id
    context.document.title = document_title
    context.document.save()


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.user = User.objects.create_reader_user(username=username, password=Faker().password())


@step("there are my personal general notes (?P<my_general_notes>.+) added by me")
def step_impl(context, my_general_notes):
    """
    :type context: behave.runner.Context
    :type my_general_notes: str
    """
    for note in my_general_notes.split(","):
        context.my_general_note = GeneralNote.objects.create()
        context.my_general_note.content = note
        context.my_general_note.date = datetime.now().date
        context.my_general_note.user = context.user
        context.my_general_note.document = context.document
        context.my_general_note.save()


@step("there are general notes (?P<general_notes>.+) added by other users")
def step_impl(context, general_notes):
    """
    :type context: behave.runner.Context
    :type general_notes: str
    """
    context.user_random = User.objects.create_reader_user(username=Faker().name(), password=Faker().password())
    context.user_random.follow(context.user)
    context.user.add_follower(context.user_random)

    for note in general_notes.split(","):
        context.general_note = GeneralNote.objects.create()
        context.general_note.content = note
        context.general_note.date = datetime.now().date
        context.general_note.user = context.user_random
        context.general_note.document = context.document
        context.general_note.save()


@when("I want to compare my notes with those of other users")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_general_notes = GeneralNoteDAO.get_personal_general_notes(context.user.username, context.document.id)
    context.general_notes = GeneralNoteDAO.get_general_notes(context.user.username, context.document.id)


@then("it should display my personal general notes (?P<my_general_notes>.+) ordered")
def step_impl(context, my_general_notes):
    """
    :type context: behave.runner.Context
    :type my_general_notes: str
    """
    expect(context.my_general_notes).to(equal(my_general_notes))


@step("the general notes (?P<general_notes>.+) from other users ordered\.")
def step_impl(context, general_notes):
    """
    :type context: behave.runner.Context
    :type general_notes: str
    """
    expect(context.general_notes).to(equal(general_notes))


@step("there are notes (?P<my_notes>.+) added by me in the page (?P<page_number>.+)")
def step_impl(context, my_notes, page_number):
    """
    :type context: behave.runner.Context
    :type my_notes: str
    :type page_number: str
    """
    for note in my_notes.split(","):
        context.my_note = PageNote.objects.create()
        context.my_note.content = note
        context.my_note.date = datetime.now().date
        context.my_note.user = context.user
        context.my_note.page = page_number
        context.my_note.document = context.document
        context.my_note.save()


@step("there are notes (?P<notes>.+) added by other users in the page (?P<page_number>.+)")
def step_impl(context, notes, page_number):
    """
    :type context: behave.runner.Context
    :type notes: str
    :type page_number: str
    """
    context.user_random = User.objects.create_reader_user(username=Faker().name(), password=Faker().password())
    context.user_random.follow(context.user)
    context.user.add_follower(context.user_random)

    for note in notes.split(","):
        context.note = PageNote.objects.create()
        context.note.content = note
        context.note.date = datetime.now().date
        context.note.user = context.user_random
        context.note.page = page_number
        context.note.document = context.document
        context.note.save()


@when("I want to compare my notes with those of other users in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    context.my_notes = PageNoteDAO.get_personal_page_notes(context.user.username, context.document.id, page_number)
    context.notes = PageNoteDAO.get_page_notes(context.user.username, context.document.id, page_number)


@then("it should display my personal notes (?P<my_notes>.+) ordered")
def step_impl(context, my_notes):
    """
    :type context: behave.runner.Context
    :type my_notes: str
    """
    expect(context.my_notes).to(equal(my_notes))


@step("the notes (?P<notes>.+) from other users ordered\.")
def step_impl(context, notes):
    """
    :type context: behave.runner.Context
    :type notes: str
    """
    expect(context.notes).to(equal(notes))
