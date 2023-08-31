import os

from behave import *

import articles
from articles import views
from articles.models import Document
from articles.services import documents_service

use_step_matcher("parse")


@given("{local_path} on the disk")
def local_path_on_the_disk(context, local_path):
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
def i_upload_the_article_subject(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
    context.document = documents_service.from_local_path(context.local_path, category=subject)


@then("the article must be on {subject_path}")
def the_article_must_be_on_subject_path(context, subject_path):
    """
    :type context: behave.runner.Context
    :type subject_path: str
    """
    print(os.path.realpath(subject_path))
    assert os.path.isfile(subject_path)


@then("{message} will be displayed")
def message_will_be_displayed(context, message):
    """
    :type context: behave.runner.Context
    :type message: str
    """
    raise NotImplementedError(u'STEP: And <message> will be displayed')


# 2
@given("{title}, {autor}, {subject}")
def title_autor_subject(context, title, autor, subject):
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
def the_article_is_uploaded(context):
    """
    :type context: behave.runner.Context
    """
    context.document = documents_service.from_local_path(
        context.local_path,
        title=context.title,
        author=context.author,
        category=context.subject
    )
<<<<<<< HEAD
    context.document.save()
=======
>>>>>>> team2-feature4
    print(f"url: {context.document.url()}")
    context.document.increase_view_count()


@then("it must auto generate a {unique_id}")
def it_must_auto_generate_a_unique_id(context, unique_id):
    """
    :type context: behave.runner.Context
    :type unique_id: str
    """
    assert context.document.uid is not None


@then("the {unique_id} index with the {subject_path}")
def the_unique_id_index_with_the_subject_path(context, unique_id, subject_path):
    """
    :type context: behave.runner.Context
    :type unique_id: str
    :type subject_path: str
    """
    assert os.path.isfile(subject_path)
    print(f"{context.documents.uid}, {unique_id}")
    assert context.documents.uid == unique_id


@then("the file is available at {subject_path} through http/s")
<<<<<<< HEAD
def the_file_is_available_at_subject_path_through_http_s(context, subject_path:str):
=======
def step_impl(context, subject_path:str):
>>>>>>> team2-feature4
    from django.test import RequestFactory
    request_factory = RequestFactory()
    my_request = request_factory.get(subject_path)
    response = views.serve_document(my_request,subject_path.lstrip("articles"))
    assert response.status_code == 200
<<<<<<< HEAD


@given('the text "{author_prefix}"')
def the_text_author_prefix(context, text):
    """
    :type context: behave.runner.Context
    :type text: str
    """
    raise NotImplementedError(u'STEP: Given the text "<text>"')


@step("a default repertoire of Authors")
def a_default_repertoire_of_authors(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a default repertoire of Authors')


@when("lookup for an author")
def lookup_for_an_author(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When lookup for an author')


@then("it must return {array} as potential authors")
def it_must_return_array_as_potential_authors(context, array):
    """
    :type context: behave.runner.Context
    :type array: str
    """
    raise NotImplementedError(u'STEP: Then it must return <array> as potential authors')


@step("a hash check is performed")
def a_hash_check_is_performed(context):
    """
    :type context: behave.runner.Context
    """
    documents_service.from_local_path(context.local_path)


@then("{warnigs} warning_s are shown")
def warnigs_warning_s_are_shown(context, warnigs):
    """
    :type context: behave.runner.Context
    :type warnigs: str
    """
    raise NotImplementedError(u'STEP: Then <warnigs> warning_s are shown')


@given("{local_path} on the disk has been uploaded")
def local_path_on_the_disk_has_been_uploaded(context, local_path):
    local_path_on_the_disk(local_path)
    the_article_is_uploaded()
=======
>>>>>>> team2-feature4
