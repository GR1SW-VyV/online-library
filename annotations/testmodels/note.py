from datetime import datetime


class Note:

    def __init__(self, note_id, content, page, user_id, document_id):
        self.note_id = note_id
        self.content = content
        self.is_important = False
        self.page = page
        self.date = datetime.now()
        self.user_id = user_id
        self.document_id = document_id

    def set_importance(self):
        self.is_important = not self.is_important




