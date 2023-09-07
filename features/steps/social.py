import datetime

import faker
from behave import *
from social.models import User
from articles.models import Document
from social.models import CollectionActivity, UserActivity
from bookcollections.models import CollectionDAO, Collection
from faker import Faker

use_step_matcher("re")


@given("that I follow a collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User()
    context.user.name = Faker().name()
    context.user.save()

    context.collection = Collection(user=User.objects.create_professor_user(username=Faker().name(), password=Faker().password()))
    context.collection.name = Faker().color_name()
    context.collection.save()

    context.user.follow(context.collection)


@when("the owner of the collection adds a new book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.document = Document.objects.create()
    context.document.title = Faker().catch_phrase()
    context.document.save()
    CollectionDAO.add_book(context.collection, context.document)

    context.activity = CollectionActivity()
    context.activity.document = context.document
    context.activity.collection = context.collection
    context.activity.detail = "add a new document"
    context.activity.date = datetime.date.today()


@then("the book will appear in my feed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    assert context.user.in_my_feed(context.activity)


@given("that there is a reader Andrés")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.andres = User.objects.create_user(
        username='andres',
        password=Faker().password(),
        first_name='Andrés',
        email=Faker().email()
    )


@step("that there is a reader Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.juan = User.objects.create_user(
        username='juan',
        password=Faker().password(),
        first_name='Juan',
        email=Faker().email()
    )


@when("Andrés follows Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.andres.follow(context.juan)


@then("Juan will appear in the list of following of Andrés")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.andres.is_following(context.juan)


@step("Andrés will appear in the list of followers of Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.juan.is_followed_by(context.andres)


@given("that I follow a reader in my tracked list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User.objects.create_user(
        username=Faker().name(),
        password=Faker().password(),
        first_name=Faker().name(),
        email=Faker().email()
    )
    context.followed_user = User.objects.create_user(
        username=Faker().name(),
        password=Faker().password(),
        first_name=Faker().name(),
        email=Faker().email()
    )
    context.user.follow(context.followed_user)


@when("the reader does a new activity")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.activity = UserActivity()
    context.activity.responsible = context.followed_user
    context.activity.detail = "does a new activity"
    context.activity.date = datetime.date.today()
    context.followed_user.do_activity()


@then("the activity will appear in the list of recent activities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.in_my_feed(context.activity)


@given("that there is a collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.collection = Collection()
    context.collection.user = User.objects.create_reader_user(
        username=Faker().user_name(),
        password=Faker().password(),
    )
    context.collection.name = Faker().color_name()
    context.collection.save()


@when("I follow the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User()
    context.user.name = Faker().name()
    context.user.save()
    context.user.follow(context.collection)


@then("the new collection will appear in my list of followed collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.is_in_my_following_collection(context.collection)
