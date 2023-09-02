from behave import *
from django.contrib.auth.models import User
from bookcollections.models import Collection, CollectionDAO, MockArticle

use_step_matcher("re")


def fake_book_dependencies(book_name):
    if book_name == "null":
        return None
    else:
        book = MockArticle.objects.create(name=book_name)
        book.save()
        return book


@given(
    "the collection's name: (?P<name>.+), "
    "description: (?P<description>.+) "
    "type of privacy: (?P<type_privacy>.+)"
)
def step_impl(context, name, description, type_privacy):
    """
    :type context: behave.runner.Context
    :type name: str
    :type description: str
    :type type_privacy: str
    """
    user = User.objects.create_user(username="user1")
    user.save()
    context.user = user
    context.input_name = name
    context.input_description = description
    context.input_privacy = type_privacy == "True"


@step("as optional a (?P<book_name>.+)")
def step_impl(context, book_name):
    """
    :type context: behave.runner.Context
    :type book_name: str
    """
    context.input_book_name = book_name
    context.book = fake_book_dependencies(book_name)


@when("the user create the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    obj = Collection.objects.create(user=context.user)
    obj.name = context.input_name
    obj.description = context.input_description
    obj.is_public = context.input_privacy
    obj.save()
    # this method must be implemented in CollectionDAO
    CollectionDAO.add_book_with_name(context.input_name, context.input_book_name)


@then(
    "the collection will be created with the name, description and type of privacy given"
)
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.collection_object = CollectionDAO.search_by_name(context.input_name).first()
    assert context.collection_object is not None
    assert context.collection_object.name == context.input_name
    assert context.collection_object.description == context.input_description
    assert context.collection_object.is_public == context.input_privacy


@step("will contain the book if it was given")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.collection_object.books.filter(name=context.input_book_name).first() == context.book
