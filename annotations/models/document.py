class Document:

    def __init__(self, title, document_id):
        self.document_id = document_id
        self.title = title
        self.listGeneralNotes = []

    def add_generalNote(self, generalNote):
        self.listGeneralNotes.append(generalNote)

    def note_in_document(self,generalNote):
        return generalNote in self.listGeneralNotes
