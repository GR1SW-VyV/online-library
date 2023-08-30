from pytest_bdd import scenario, given, when, then


@given("I am reading a document <name_document>")
def step_impl(name_document):
    raise NotImplementedError(u'STEP: Given I am reading a document <name_document>')


@when("I add a note with the text <note_text> of page <number_page>")
def step_impl(note_text, number_page):
    raise NotImplementedError(u'STEP: When I add a note with the text <note_text> of page <number_page>')


@then("I should see the note in the notes section")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should see the note in the notes section')


@given("I am seeing the document information about <name_document>")
def step_impl(name_document):
    raise NotImplementedError(u'STEP: Given I am seeing the document information about <name_document>')


@when("I add an note with the text <annotation_text>")
def step_impl(annotation_text):
    raise NotImplementedError(u'STEP: When I add an note with the text <annotation_text>')


@then("I should see the note with the information of the document")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should see the note with the information of the document')


@when("I mark the note as favorite")
def step_impl():
    raise NotImplementedError(u'STEP: When I mark the note as favorite')


@then("I should see the note with the mark")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should see the note with the mark')