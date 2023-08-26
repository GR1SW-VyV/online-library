import faker
from behave import *
from social.models.user import User
from social.models.collection import Collection
from social.models.document import Document
from social.models.activity import Activity, CollectionActivity
from faker import Faker


use_step_matcher("re")


@given(": that I follow a collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User()
    context.user.name = Faker().name()

    context.collection = Collection()
    context.collection.name = Faker().color_name()

    context.user.follow(context.collection)




@when(": the owner of the collection adds a new book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.document = Document
    context.document.title = Faker().catch_phrase()
    context.collection.add_document(context.document)
    context.activity = CollectionActivity()
    context.activity.document = context.document
    context.activity.observable = context.collection
    context.activity.detail = "add a new document"



@then(": the book will appear in my feed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.in_my_feed(context.activity)


@given(": that there is a reader Andrés")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.andres = User()
    context.andres.name = "Andrés"



@step("that there is a reader Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.juan = User()
    context.juan.name = "Juan"

@when(": Andrés follows Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.andres.follow(context.juan)

@then(": Juan will appear in the list of following of Andrés")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.andres.is_following(context.juan)


@step(": Andrés will appear in the list of followers of Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.juan.is_followed_by(context.andres)


@given(": that I follow a reader in my tracked list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User()
    context.user.name = Faker().name()
    context.followed_user = User()
    context.followed_user.name = Faker().name()
    context.user.follow(context.followed_user)


@when(": the reader does a new activity")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.activity = Activity()
    context.activity.observable = context.followed_user
    context.activity.detail = "does a new activity"
    context.followed_user.do_activity()


@then(": the activity will appear in the list of recent activities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.in_my_feed(context.activity)



@given(": that there is a collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.collection = Collection()
    context.collection.name = Faker().color_name()


@when(": I follow the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User()
    context.user.name = Faker().name()
    context.user.follow(context.collection)

@then(": the new collection will appear in my list of followed collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.is_in_my_following_collection(context.collection)