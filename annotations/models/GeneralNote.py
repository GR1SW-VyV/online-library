from datetime import datetime


class GeneralNote:

    def __init__(self, content, user_id, document_id):
        self.content = content
        self.date = datetime.now()
        self.user_id = user_id
        self.document_id = document_id
