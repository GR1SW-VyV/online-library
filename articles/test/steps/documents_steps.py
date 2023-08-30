import os

from behave import *

import articles
from articles import views
from articles.models import Document
from articles.services import documents_service

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
    context.document = documents_service.from_local_path(context.local_path, category=subject)


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
    context.document = documents_service.from_local_path(
        context.local_path,
        title=context.title,
        author=context.author,
        category=context.subject
    )
    print(f"url: {context.document.url()}")
    context.document.increase_view_count()


@then("it must auto generate a {unique_id}")
def step_impl(context, unique_id):
    """
    :type context: behave.runner.Context
    :type unique_id: str
    """
    assert context.document.uid is not None


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


@then("the file is available at {subject_path} through http/s")
def step_impl(context, subject_path:str):
    from django.test import RequestFactory
    request_factory = RequestFactory()
    my_request = request_factory.get(subject_path)
    response = views.serve_document(my_request,subject_path.lstrip("articles"))
    assert response.status_code == 200
