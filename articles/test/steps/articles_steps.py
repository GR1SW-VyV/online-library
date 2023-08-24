import os


from behave import *

import articles
from articles.services import article

use_step_matcher("parse")


@given("{local_path} on the disk")
def step_impl(context, local_path):
    """
    :type context: behave.runner.Context
    :type local_path: str
    """
    context.local_path = local_path
    print(os.path.realpath(local_path))
    with open(local_path,'w') as f:
        f.write("sample")
    assert os.path.isfile(local_path)


@when("I upload the article as {subject}")
def step_impl(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
    context.article = article.from_local_path(context.local_path, subject=subject)


@then("the article must be on {subject_path}")
def step_impl(context, subject_path):
    """
    :type context: behave.runner.Context
    :type subject_path: str
    """
    print(os.path.realpath(subject_path))
    assert os.path.isfile(subject_path)


@then("{message} will be displayed")
def step_impl(context, message):
    """
    :type context: behave.runner.Context
    :type message: str
    """
    raise NotImplementedError(u'STEP: And <message> will be displayed')

