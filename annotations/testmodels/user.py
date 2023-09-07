from .note import Note


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.listNotes = []

    def add_note(self, note):
        self.listNotes.append(note)

    def get_note_by_id(self, note_id):
        for note in self.listNotes:
            if note.note_id == note_id:
                return note
            return None
