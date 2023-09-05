from behave import *
from ....models import MockUser, MockDocuments,MockCollections
use_step_matcher("re")




@given("users has no collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    #context.user = MockUser.objects.create()
    assert not context.user.has_collections()


@step("send preferences (?P<preference1>.+) (?P<preference2>.+) (?P<preference3>.+)")
def step_impl(context, preference1, preference2, preference3):
    """
    :type context: behave.runner.Context
    :type preference1: str
    :type preference2: str
    :type preference3: str
    """
    context.MockUser.recive_preferences(preference1, preference2, preference3)

@when("the reader wants recommendations")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.recomendations = context.MockUser.get_recomendations()


@then("a set of (?P<num_recomendations>.+) most visited readings of (?P<preference1>.+) are recommended")
def step_impl(context, num_recomendations, preference1):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference1: str
    """
    context.num_recomendations, context.preference1 = next(context.MockUser.recomendation_by_category())



@step("a set of (?P<num_recomendations>.+) most visited readings of (?P<preference2>.+) are recommended")
def step_impl(context, num_recomendations, preference2):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference2: str
    """
    context.num_recomendations, context.preference2 = next(context.MockUser.recomendation_by_category())


@step("a set of (?P<num_recomendations>.+) most visited readings of (?P<preference3>.+) are recommended")
def step_impl(context, num_recomendations, preference2):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference2: str
    """
    context.num_recomendations, context.preference3 = next(context.MockUser.recomendation_by_category())



@given("users has collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.has_collections()


@step("have this most common categories (?P<category1>.+) (?P<category2>.+) (?P<category3>.+)")
def step_impl(context, category1, category2, category3):
    """
    :type context: behave.runner.Context
    :type category1: str
    :type category2: str
    :type category3: str
    """
    context.category1, context.category2, context.category3 = context.MockUser.get_top_categories()