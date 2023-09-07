import hashlib
import json
import os

import faker
from behave import *

import articles
from articles import views
from articles.models import Document, Author
from articles.services import documents_service

use_step_matcher("parse")

def hash_int(x:str,/):
    return int.from_bytes(hashlib.md5(x.encode('utf8')).digest()) % (2 ** 32)

@given("{local_path} on the disk")
def local_path_on_the_disk(context, local_path):
    """
    :type context: behave.runner.Context
    :type local_path: str
    """
    context.local_path = local_path
    if not os.path.isfile(local_path):
        import random
        with open(local_path, 'wb') as f:
            f.write(random.randbytes(1024))


@when("I upload the article as {subject}")
def i_upload_the_article_subject(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
    context.document = documents_service.from_local_path(context.pdf_path, category=subject)


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
    context.document.save()
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
    assert context.documents.uid == unique_id


@then("the file is available at {subject_path} through http/s")
def the_file_is_available_at_subject_path_through_http_s(context, subject_path: str):
    from django.test import RequestFactory
    request_factory = RequestFactory()
    my_request = request_factory.get(subject_path)
    response = views.serve_document(my_request, subject_path.lstrip("articles"))
    assert response.status_code == 200


@given('the text "{author_prefix}"')
def the_text_author_prefix(context, author_prefix):
    """
    :type context: behave.runner.Context
    :type author_prefix: str
    """
    context.author_prefix = author_prefix


@step("a default repertoire of Authors")
def a_default_repertoire_of_authors(context):
    """
    :type context: behave.runner.Context
    """
    a1 = Author(name="Baldor Aurelio")
    a2 = Author(name="Balaca Ricardo")
    a3 = Author(name="Berro Adolfo")
    for a in [a1, a2, a3]: a.save()


@when("lookup for an author")
def lookup_for_an_author(context):
    """
    :type context: behave.runner.Context
    """
    context.suggested_authors = Author.get_by_prefix(context.author_prefix)


@then("it must return {array} as potential authors")
def it_must_return_array_as_potential_authors(context, array):
    """
    :type context: behave.runner.Context
    :type array: str
    """
    authors_json = json.dumps(list(a.name for a in context.suggested_authors))
    assert array == authors_json


@step("a hash check is performed")
def a_hash_check_is_performed(context):
    """
    :type context: behave.runner.Context
    """

    context.collision = Document.find_colliding_document(context.local_path)


@given("{local_path} on the disk has been uploaded")
def local_path_on_the_disk_has_been_uploaded(context, local_path):
    local_path_on_the_disk(context, local_path)
    the_article_is_uploaded(context)


@then("no collision is found")
def no_collision_is_found(context):
    """
    :type context: behave.runner.Context
    :type warnings: str
    """
    assert context.collision is None
    assert context.collision is None


@then("a collision is found")
def a_collision_is_found(context):
    """
    :type context: behave.runner.Context
    :type warnings: str
    """
    assert context.collision is not None


@then("one collision/s were/was found")
def a_colliding_file_is_shown(context):
    """
    :type context: behave.runner.Context
    :type warnings: str
    """
    # raise NotImplementedError(u'STEP: And <warnings> colliding file is shown')


@then("zero collision/s were/was found")
def no_colliding_file_is_shown(context):
    """
    :type context: behave.runner.Context
    :type warnings: str
    """
    # raise NotImplementedError(u'STEP: And <warnings> colliding file is shown')


@step("{} scores the document a {}")
def step_impl(context, arg0, arg1):
    """
    :type context: behave.runner.Context
    """
    user = int(arg0)
    score = int(arg1)
    context.document.add_score(user, score)


@then("the final score must be {}")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    """
    score = float(arg0)
    assert context.document.score() == score


@step("a pdf file {filename}")
def given_a_pdf_file_on_disk(context, filename):
    path = f"tmp/{filename}"
    context.pdf_path = f"tmp/{filename}"
    print(path)
    if not os.path.isfile(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        import random
        with open(path, 'wb') as f:
            f.write(random.randbytes(1024))

@then("document {}'s final score must be {}")
def step_impl(context, arg0, arg1):
    """
    :type context: behave.runner.Context
    """
    document: Document = context.document[arg0]
    final_score = float(arg1)
    assert document.score() == final_score

@step("{} scores document {} a {}")
def x_scores_document_y_a_z(context, arg0, arg1, arg2):
    """
    :type context: behave.runner.Context
    """
    user = hash_int(arg0)
    document: Document = context.document[arg1]
    score = int(arg2)

    document.add_score(user, score)

@given("a document {document_alias}")
def given_a_document(context, document_alias):
    given_a_pdf_file_on_disk(context, document_alias)
    doc = documents_service.from_local_path(
        f"tmp/{document_alias}.pdf",
        title=context.fake.address(),
        author=context.fake.name(),
        category=context.fake.category(),
        type=context.fake.document_type()
    )
    doc.save()
    context.document[document_alias] = doc


@when("a {document_alias} hash check is performed on {pdf_file}")
def step_impl(context, document_alias,pdf_file):
    document: Document = context.document[document_alias]

    context.collision = document.find_colliding_document(f"tmp/{pdf_file}")

