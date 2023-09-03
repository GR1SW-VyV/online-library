from behave import *

use_step_matcher("re")


@given("this preferences (?P<preference1>.+) (?P<preference2>.+) (?P<preference3>.+)")
def step_impl(context, preference1, preference2, preference3):
    """
    :type context: behave.runner.Context
    :type preference1: str
    :type preference2: str
    :type preference3: str
    """

    context.user_preference1 = User.get_reference()
    context.user_preference2 = User.get_reference()
    context.user_preference3 = User.get_reference()
    assert context.user_preference1 == preference1
    assert context.user_preference2 == preference2
    assert context.user_preference3 == preference2

@step("users has no collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And users has no collections')
    context.user = User.veryfi_collections()


@when("he wants recommendations")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When he wants recommendations')
    context.user = User.generate_recommendations()


@then("a set of (?P<num_recomendations>.+) most visited readings of (?P<preference1>.+) are recommended")
def step_impl(context, num_recomendations, preference1):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference1: str
    """
    context.user_categoria1 = User.get_reference()
    context.user_size_categoria1 = User.get_size_reference
    assert context.user_categoria1 == preference1
    assert context.user_size_categoria1 == num_recomendations


@step("a set of (?P<num_recomendations>.+) most visitedreadings of (?P<preference2>.+) are recommended")
def step_impl(context, num_recomendations, preference2):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference2: str
    """
    context.user_categoria2 = User.get_reference()
    context.user_size_categoria2 = User.get_size_reference
    assert context.user_categoria2 == preference2
    assert context.user_size_categoria2 == num_recomendations


"""--------------Scenario Outline: Recommendations based on a collection --------------"""


class User:
    pass


@given("this most common categories (?P<category1>.+) (?P<category2>.+) (?P<category3>.+)")
def step_impl(context, category1, category2, category3):
    """
    :type context: behave.runner.Context
    :type category1: str
    :type category2: str
    :type category3: str
    """
    context.user_preference1 = User.get_reference()
    context.user_preference2 = User.get_reference()
    context.user_preference3 = User.get_reference()
    assert context.user_preference1 == category1
    assert context.user_preference2 == category2
    assert context.user_preference3 == category3

@step("there are books that do not belong to the user collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User.check_books_without_collection()

@when("the reader wants recommendations")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = User.generate_recommendations()
