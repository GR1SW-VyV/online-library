from behave import *
from expects import *
from faker import Faker

from articles.models import Document
from social.models import User
from visualization.models import GeneralNote, GeneralNoteDAO, PageNote, PageNoteDAO

use_step_matcher("re")


@given("I have the document (?P<document_title>.+) with the id (?P<document_id>.+)")
def step_impl(context, document_title, document_id):
    """
    :type context: behave.runner.Context
    :type document_title: str
    :type document_id: str
    """
    context.document = Document.objects.get_or_create(title=document_title)[0]


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.user = User.objects.create_reader_user(username=username, password=Faker().password())


@step("there are notes (?P<my_general_notes>.+) added by me on (?P<date>.+) date")
def step_impl(context, my_general_notes, date):
    """
    :type context: behave.runner.Context
    :type my_general_notes: str
    :type date: str
    """
    for note, date in zip(my_general_notes.split(","), date.split(",")):
        context.my_general_note = GeneralNote.objects.create(
            content=note,
            date=date,
            user=context.user,
            document=context.document
        )


@when("I want to read my notes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_general_notes = GeneralNoteDAO.get_personal_general_notes(context.user.username, context.document.uid)


@then("it should display my personal notes (?P<my_ordered_general_notes>.+) ordered by date")
def step_impl(context, my_ordered_general_notes):
    """
    :type context: behave.runner.Context
    :type my_ordered_general_notes: str
    """
    expect(GeneralNoteDAO.get_str_general_notes(context.my_general_notes)).to(equal(my_ordered_general_notes))


@step(
    "there are notes (?P<my_page_notes>.+) added by me in the page (?P<page_number>.+) on (?P<date>.+) date marked as (?P<is_favorite>.+) favorite")
def step_impl(context, my_page_notes, page_number, date, is_favorite):
    """
    :type context: behave.runner.Context
    :type my_page_notes: str
    :type page_number: str
    :type date: str
    :type is_favorite: str
    """
    for note, date, favorite in zip(my_page_notes.split(","), date.split(","), is_favorite.split(",")):
        context.my_page_note = PageNote.objects.create(
            content=note,
            date=date,
            is_favorite=favorite,
            page=page_number,
            user=context.user,
            document=context.document
        )


@when("I want to read my notes in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    context.my_page_notes = PageNoteDAO.get_personal_page_notes(context.user.username, context.document.uid, page_number)


@then("it should display my personal notes (?P<my_ordered_page_notes>.+) ordered by date and favorite")
def step_impl(context, my_ordered_page_notes):
    """
    :type context: behave.runner.Context
    :type my_ordered_page_notes: str
    """
    expect(PageNoteDAO.get_str_page_notes(context.my_page_notes)).to(equal(my_ordered_page_notes))


@step(
    "there are general notes (?P<general_notes>.+) added by other users who are (?P<user_type>.+) with (?P<followers>.+) followers on (?P<date>.+) date")
def step_impl(context, general_notes, user_type, followers, date):
    for note, date, user_type in zip(general_notes.split(","), date.split(","), user_type.split(",")):
        context.general_note = GeneralNote.objects.create(
            content=note,
            date=date,
            user= User.objects.create_reader_user(username=Faker().name(), password=Faker().password()) if user_type == "reader" else User.objects.create_professor_user(username=Faker().name(), password=Faker().password()),
            document=context.document
        )


@when("I want to read the general notes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.general_notes = GeneralNoteDAO.get_general_notes(context.user.username, context.document.uid)


@then("it should display the general notes (?P<ordered_general_notes>.+) ordered by date")
def step_impl(context, ordered_general_notes):
    """
    :type context: behave.runner.Context
    :type ordered_general_notes: str
    """
    expect(GeneralNoteDAO.get_str_general_notes(context.general_notes)).to(equal(ordered_general_notes))


@step(
    "there are notes (?P<page_notes>.+) added by other users who are (?P<user_type>.+) with (?P<followers>.+) followers in the page (?P<page_number>.+) on (?P<date>.+) date marked as (?P<is_favorite>.+) favorite")
def step_impl(context, page_notes, user_type, followers, page_number, date, is_favorite):
    """
    :type context: behave.runner.Context
    :type page_notes: str
    :type user_type: str
    :type followers: str
    :type page_number: str
    :type date: str
    :type is_favorite: str
    """
    for note, page, date, favorite in zip(page_notes.split(","), page_number.split(","), date.split(","),
                                          is_favorite.split(",")):
        context.page_note = PageNote.objects.create(
            content=note,
            date=date,
            is_favorite=favorite,
            page=page,
            user=User.objects.create_reader_user(username=Faker().name(), password=Faker().password()),
            document=context.document
        )


@when("I want to read the notes in the page (?P<page_number>.+)")
def step_impl(context, page_number):
    """
    :type context: behave.runner.Context
    :type page_number: str
    """
    context.page_notes = PageNoteDAO.get_page_notes(context.user.username, context.document.uid, page_number)


@then("it should display the notes (?P<ordered_page_notes>.+) ordered by date and favorite")
def step_impl(context, ordered_page_notes):
    """
    :type context: behave.runner.Context
    :type ordered_page_notes: str
    """
    expect(PageNoteDAO.get_str_page_notes(context.page_notes)).to(equal(ordered_page_notes))


