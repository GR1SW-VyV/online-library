from behave import *

use_step_matcher("re")


@given("the (?P<path>.+) of the article")
def step_impl(context, path):
    """
    :type context: behave.runner.Context
    :type path: str
    """
    raise NotImplementedError(u'STEP: Given the <path> of the article')


@when("I upload the article")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I upload the article')


@then("if the upload was successful or not there will be a (?P<response>.+)")
def step_impl(context, response):
    """
    :type context: behave.runner.Context
    :type response: str
    """
    raise NotImplementedError(u'STEP: Then if the upload was successful or not there will be a <response>')