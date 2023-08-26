from social.models.observable import Observable


class Collection(Observable):
    name = ""
    documents = []

    def add_document(self, document):
        pass

    def notify(self):
        pass
