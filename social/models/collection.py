from social.models.activity import CollectionActivity
from social.models.observable import Observable


class Collection(Observable):
    name = ""
    documents = []

    def add_document(self, document):
        self.documents.append(document)
        activity = self.create_collection_activity(document)
        self.add_activity(activity)

    def create_collection_activity(self, document):
        activity = CollectionActivity()
        activity.document = document
        activity.observable = self
        activity.detail = "add a new document"
        return activity

    def notify(self):
        for observer in self.followers:
            observer.update(self.activities[-1])