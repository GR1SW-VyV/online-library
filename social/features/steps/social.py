from behave import *

use_step_matcher("re")


@given(": that I follow a collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given : that I follow a collection')


@when(": the owner of the collection adds a new book")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When : the owner of the collection adds a new book')


@then(": the book will appear in my feed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then : the book will appear in my feed')


@given(": that there is a reader Andrés")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given : that there is a reader Andrés')


@step("that there is a reader Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And that there is a reader Juan')


@when(": Andrés follows Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When : Andrés follows Juan')


@then(": Juan will appear in the list of following of Andrés")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then : Juan will appear in the list of following of Andrés')


@step(": Andrés will appear in the list of followers of Juan")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And : Andrés will appear in the list of followers of Juan')


@given(": that I follow a reader in my tracked list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given : that I follow a reader in my tracked list')


@when(": the reader does a new activity")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When : the reader do a new activity')


@then(": the activity will appear in the list of recent activities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then : the activity will appear in the list of recent activities')


@given(": that there is a collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given : that there is a collection')


@when(": I follow the collection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When : I follow the collection')


@then(": the new collection will appear in my list of followed collections")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then : the new collection will appear in my list of followed collections')