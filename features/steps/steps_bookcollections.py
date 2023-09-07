from behave import *
from social.models import User
from bookcollections.models import Collection, CollectionDAO
from articles.models import Document
from faker import Faker

use_step_matcher("re")
fake = Faker()


def fake_book_dependencies(book_name, book_score):
    if book_name == "null":
        return None
    else:
        book = Document.objects.create(title=book_name)
        book.add_score(1, book_score)
        book.save()
        return book


@given(
    "the collection's name: (?P<name>.+), "
    "a description and type of privacy: (?P<is_private>.+)"
)
def step_impl(context, name, is_private):
    """
    :type context: behave.runner.Context
    :type name: str
    :type is_private: bool
    """
    user = User.objects.create_user(username="user1")
    user.save()
    context.user = user
    context.input_name = name
    context.input_description = fake.text()
    context.input_privacy = is_private == "True"


@step("the book (?P<book_name>.+) with (?P<book_score>.+) points")
def step_impl(context, book_name, book_score):
    """
    :param book_score:
    :type context: behave.runner.Context
    :type book_name: str
    """
    context.input_book_name = book_name
    context.input_book_score = float(book_score)
    context.book = fake_book_dependencies(book_name, context.input_book_score)


@when("the user creates the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    obj = Collection.objects.create(user=context.user)
    obj.name = context.input_name
    obj.description = context.input_description
    obj.is_public = context.input_privacy
    obj.save()
    CollectionDAO.add_book_with_name(context.input_name, context.input_book_name)


@then(
    "the collection will be created with the given name, "
    "description and type of privacy"
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


@step("will contain the given book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert (
        context.collection_object.books.filter(title=context.input_book_name).first()
        == context.book
    )


@step("will have (?P<collection_score>.+) points")
def step_impl(context, collection_score):
    """
    :type context: behave.runner.Context
    :type collection_score: str
    """
    assert context.collection_object.score == float(context.input_book_score)


# Second Scenario
@given("the collection with two books")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = User.objects.create_user(username="user2")
    user.save()
    context.user = user
    obj2 = Collection.objects.create(user=context.user)
    context.collection_name = fake.catch_phrase()
    obj2.name = context.collection_name
    obj2.description = fake.text()
    obj2.is_public = True
    obj2.save()
    context.input_book_1 = fake.catch_phrase()
    context.input_book_2 = fake.catch_phrase()


@step("their respective points: (?P<book_score_1>.+), (?P<book_score_2>.+)")
def step_impl(context, book_score_1, book_score_2):
    """
    :type context: behave.runner.Context
    :type book_score_1: str
    :type book_score_2: str
    """
    context.input_score_1 = float(book_score_1)
    context.input_score_2 = float(book_score_2)

    context.book_1 = fake_book_dependencies(
        context.input_book_1, context.input_score_1)
    context.book_2 = fake_book_dependencies(
        context.input_book_2, context.input_score_2)

    CollectionDAO.add_book_with_name(
        context.collection_name, context.input_book_1)
    CollectionDAO.add_book_with_name(
        context.collection_name, context.input_book_2)


@step("the user want to add a new book with (?P<book_score_3>.+) points")
def step_impl(context, book_score_3):
    """
    :type context: behave.runner.Context
    :type book_score_3: str
    """
    context.input_book_3 = fake.catch_phrase()
    context.input_score_3 = float(book_score_3)
    context.book_3 = fake_book_dependencies(
        context.input_book_3, context.input_score_3)


@when("the user adds the book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    CollectionDAO.add_book_with_name(context.collection_name, context.input_book_3)


@then(
    "the collection score will be (?P<collection_points>.+) "
    "representing average points of all books"
)
def step_impl(context, collection_points):
    """
    :type context: behave.runner.Context
    :type collection_points: str
    """
    context.input_expected_score = float(collection_points)
    object = CollectionDAO.search_by_name(context.collection_name).first()
    print(type(context.input_expected_score), type(object.score))
    assert float(object.score) == context.input_expected_score
