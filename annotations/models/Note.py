from datetime import datetime


class Note:

    def __init__(self, content, is_important, page, user_id, document_id):
        self.content = content
        self.is_important = is_important
        self.page = page
        self.date = datetime.now()
        self.user_id = user_id
        self.document_id = document_id
