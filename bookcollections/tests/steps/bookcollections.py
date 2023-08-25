from behave import *

use_step_matcher("re")


@given("a collection's name: (?P<name_collection>.+) and the book: (?P<name_book>.+)")
def step_impl(context, name_collection, name_book):
    """
    :type context: behave.runner.Context
    :type name_collection: str
    :type name_book: str
    """
    raise NotImplementedError(u'STEP: Given a collection\'s name: <name_collection> and the book: <name_book>')


@when("the user add the book to collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user add the book to collection')


@then("the book will be displayed into the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the book will be displayed into the collection')


@given(
    "the collection's name: (?P<name>.+), description: (?P<description>.+) and type of privacy: (?P<type_privacy>.+)")
def step_impl(context, name, description, type_privacy):
    """
    :type context: behave.runner.Context
    :type name: str
    :type description: str
    :type type_privacy: str
    """
    raise NotImplementedError(
        u'STEP: Given the collection\'s name: <name>, description: <description> and type of privacy: <type_privacy>')


@when("the user create the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user create the collection')


@then("the collection will be created with the information given")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the collection will be created with the information given')