from social.models.document import Document
from social.models.observable import Observable
from typing import List


class Collection(Observable):
    name = ""
    documents: List[Document] = []

    def add_document(self, document: Document):
        pass

    def notify(self):
        pass
