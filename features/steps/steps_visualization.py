# Standard module imports
from behave import *

# Third party module imports
from expects import *
from faker import Faker

# Local module imports
from articles.models import Document
from social.models import User
from visualization.models import GeneralNote, GeneralNoteDAO
from annotations.models import PageNote, PageNoteDAO

use_step_matcher("re")


@given("I have the document (?P<document_title>.+)")
def step_impl(context, document_title):
    """
    :type context: behave.runner.Context
    :type document_title: str
    """
    context.document = Document.objects.get_or_create(title=document_title)[0]


@step("I am logged in with my username (?P<username>.+)")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.user = User.objects.create_reader_user(username=username, password=Faker().password())


@step(
    "there are general notes (?P<general_notes>.+) added by other users who are (?P<user_types>.+) with ("
    "?P<followers>.+) followers on (?P<dates>.+) date")
def step_impl(context, general_notes, user_types, followers, dates):
    """
    :type context: behave.runner.Context
    :type general_notes: str
    :type user_types: str
    :type followers: str
    :type dates: str
    """
    for note, date, user_type, followers in zip(general_notes.split(","), dates.split(","), user_types.split(","),
                                                followers.split(",")):
        context.general_note = GeneralNote.objects.create(
            content=note,
            date=date,
            user=User.objects.create_reader_user(username=Faker().name(),
                                                 password=Faker().password()) if user_type == "reader" else User.objects
            .create_professor_user(username=Faker().name(), password=Faker().password()),
            document=context.document
        )
        for i in range(int(followers)):
            context.follower = User.objects.create_reader_user(username=Faker().name(), password=Faker().password())
            context.follower.follow(context.general_note.user)


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
    "there are notes (?P<page_notes>.+) added by other users who are (?P<user_types>.+) with (?P<followers>.+) "
    "followers in the page (?P<page_number>.+) on (?P<dates>.+) date marked as (?P<favorites>.+) favorite")
def step_impl(context, page_notes, user_types, followers, page_number, dates, favorites):
    """
    :type context: behave.runner.Context
    :type page_notes: str
    :type user_types: str
    :type followers: str
    :type page_number: str
    :type dates: str
    :type favorites: str
    """
    for note, date, favorite, user_type, followers in zip(page_notes.split(","), dates.split(","),
                                                          favorites.split(","), user_types.split(","),
                                                          followers.split(",")):
        context.page_note = PageNote.objects.create(
            content=note,
            date=date,
            is_favorite=favorite,
            page=page_number,
            user=User.objects.create_reader_user(username=Faker().name(),
                                                 password=Faker().password()) if user_type == "reader" else User.objects
            .create_professor_user(username=Faker().name(), password=Faker().password()),
            document=context.document
        )
        for i in range(int(followers)):
            context.follower = User.objects.create_reader_user(username=Faker().name(), password=Faker().password())
            context.follower.follow(context.page_note.user)


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
