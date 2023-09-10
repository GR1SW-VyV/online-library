class Document:

    def __init__(self, title, document_id):
        self.document_id = document_id
        self.title = title
        self.listGeneralNotes = []
        self.listNotePages = []


    def add_generalNote(self, generalNote):
        self.listGeneralNotes.append(generalNote)

    def note_in_document(self,generalNote):
        return generalNote in self.listGeneralNotes

    def add_notePage(self, notePage):
        self.listNotePages.append(notePage)

    def notePage_in_document(self, notePage):
        return notePage in self.listNotePages
