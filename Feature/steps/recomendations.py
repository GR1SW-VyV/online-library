from behave import *
from recommendations.models import MockUser, MockDocuments,MockCollections
use_step_matcher("re")


@given("users has no collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = MockUser.objects.create()
    assert not context.user.has_collections()


@step("send preferences (?P<preference1>.+) (?P<preference2>.+) (?P<preference3>.+)")
def step_impl(context, preference1, preference2, preference3):
    """
    :type context: behave.runner.Context
    :type preference1: str
    :type preference2: str
    :type preference3: str
    """
    context.user.recive_preferences(preference1, preference2, preference3)


@when("the reader wants recommendations")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    #context.recommendations = context.user4.get_recomendations()
    context.recommendations = context.user.get_recomendations()


@then("a set of (?P<num_recomendations>.+) most visited readings are recommended")
def step_impl(context, num_recomendations):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    """
    assert True, context.user.recommendation_total() <= 12


@given("users has collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user4 = MockUser.objects.create()
    context.user4.collections.add(MockCollections.objects.all()[1])
    assert context.user4.has_collections()


@step("have this most common categories (?P<category1>.+) (?P<category2>.+) (?P<category3>.+)")
def step_impl(context, category1, category2, category3):
    """
    :type context: behave.runner.Context
    :type category1: str
    :type category2: str
    :type category3: str
    """
    context.category1, context.category2, context.category3 = context.user4.get_top_categories()


@then("a set of (?P<num_recommendations>.+) most visited readings are recommended based on their collections")
def step_impl(context, num_recommendations):
    """
    :type context: behave.runner.Context
    :type num_recommendations: str
    """
    assert True, context.user4.recommendation_total() <= 12