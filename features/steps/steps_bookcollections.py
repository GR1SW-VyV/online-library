from behave import *
from steps_bookcollections.models import Collection, CollectionDAO, MockArticle

use_step_matcher("re")
MockArticle.objects.create(name="Baldor's Algebra").save()

@given("the collection's name: (?P<name>.+), description: (?P<description>.+) type of privacy: (?P<type_privacy>.+)")
def step_impl(context, name, description, type_privacy):
    """
    :type context: behave.runner.Context
    :type name: str
    :type description: str
    :type type_privacy: str
    """
    context.input_name = name
    context.input_description = description
    context.input_privacy = type_privacy == "True"

@step("as optional a (?P<book_name>.+)")
def step_impl(context, book_name):
    """
    :type context: behave.runner.Context
    :type book_name: str
    """

    MockArticle.objects.create(name=book_name).save()
    context.input_book_name = book_name


@when("the user create the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    obj = Collection.objects.create()
    obj.name = context.input_name
    obj.description = context.input_description
    obj.is_public = context.input_privacy
    obj.save()
    CollectionDAO.add_book_with_name(context.input_name, context.input_book_name)


@then("the collection will be created with the name, description and type of privacy given")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.collection_object = CollectionDAO.search_by_name(context.input_name).first()
    print(context.collection_object)
    assert context.collection_object.name == context.input_name
    assert context.collection_object.description == context.input_description
    assert context.collection_object.is_public == context.input_privacy


@step("with the book if it was given")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.collection_object.books.name, context.input_book_name)
    assert context.collection_object.books.name == context.input_book_name

