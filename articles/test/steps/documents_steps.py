import os

from behave import *

import articles
<<<<<<< HEAD:articles/test/steps/articles_steps.py
from articles.services import documents_service
=======
from articles.services import documents
>>>>>>> 41864e09a53208b7b3cf8ad83f65b56c978244d3:articles/test/steps/documents_steps.py

use_step_matcher("parse")


@given("{local_path} on the disk")
def step_impl(context, local_path):
    """
    :type context: behave.runner.Context
    :type local_path: str
    """
    context.local_path = local_path
    print(os.path.realpath(local_path))
    with open(local_path, 'w') as f:
        f.write("sample")
    assert os.path.isfile(local_path)


@when("I upload the article as {subject}")
def step_impl(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
<<<<<<< HEAD:articles/test/steps/articles_steps.py
    context.article = documents_service.from_local_path(context.local_path, category=subject)
=======
    context.documents = documents.from_local_path(context.local_path, category=subject)
>>>>>>> 41864e09a53208b7b3cf8ad83f65b56c978244d3:articles/test/steps/documents_steps.py


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


# 2
@given("{title}, {autor}, {subject}")
def step_impl(context, title, autor, subject):
    """
    :type context: behave.runner.Context
    :type title: str
    :type autor: str
    :type subject: str
    """
    context.title = title
    context.author = autor
    context.subject = subject


@when("the article is uploaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
<<<<<<< HEAD:articles/test/steps/articles_steps.py
    context.article = documents_service.from_local_path(
=======
    context.documents = documents.from_local_path(
>>>>>>> 41864e09a53208b7b3cf8ad83f65b56c978244d3:articles/test/steps/documents_steps.py
        context.local_path,
        title=context.title,
        author=context.author,
        category=context.subject
    )


@then("it must auto generate a {unique_id}")
def step_impl(context, unique_id):
    """
    :type context: behave.runner.Context
    :type unique_id: str
    """
    assert context.documents.uid is not None


@then("the {unique_id} index with the {subject_path}")
def step_impl(context, unique_id, subject_path):
    """
    :type context: behave.runner.Context
    :type unique_id: str
    :type subject_path: str
    """
    assert os.path.isfile(subject_path)
    print(f"{context.documents.uid}, {unique_id}")
    assert context.documents.uid == unique_id
