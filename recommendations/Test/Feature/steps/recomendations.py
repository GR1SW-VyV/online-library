from behave import *

use_step_matcher("re")


@given("users has no collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given users has no collections')


@step("send preferences (?P<preference1>.+) (?P<preference2>.+) (?P<preference3>.+)")
def step_impl(context, preference1, preference2, preference3):
    """
    :type context: behave.runner.Context
    :type preference1: str
    :type preference2: str
    :type preference3: str
    """
    raise NotImplementedError(u'STEP: And send preferences <preference1> <preference2> <preference3>')


@when("the reader wants recommendations")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the reader wants recommendations')


@then("a set of (?P<num_recomendations>.+) most visited readings of (?P<preference1>.+) are recommended")
def step_impl(context, num_recomendations, preference1):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference1: str
    """
    raise NotImplementedError(
        u'STEP: Then a set of <num_recomendations> most visited readings of <preference1> are recommended')


@step("a set of (?P<num_recomendations>.+) most visitedreadings of (?P<preference2>.+) are recommended")
def step_impl(context, num_recomendations, preference2):
    """
    :type context: behave.runner.Context
    :type num_recomendations: str
    :type preference2: str
    """
    raise NotImplementedError(
        u'STEP: And a set of <num_recomendations> most visitedreadings of <preference2> are recommended')


@given("users has collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given users has collections')


@step("have this most common categories (?P<category1>.+) (?P<category2>.+) (?P<category3>.+)")
def step_impl(context, category1, category2, category3):
    """
    :type context: behave.runner.Context
    :type category1: str
    :type category2: str
    :type category3: str
    """
    raise NotImplementedError(u'STEP: And have this most common categories <category1> <category2> <category3>')