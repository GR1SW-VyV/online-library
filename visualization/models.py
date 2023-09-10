from django.db import models

from articles.models import Document
from social.models import User


class GeneralNote(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class GeneralNoteDAO:
    @classmethod
    def get_general_notes(cls, username, document_id):
        notes = GeneralNote.objects.all().exclude(user__username=username).filter(document__uid=document_id)
        ordered_notes = list(notes)
        ordered_notes.sort(key=lambda note: note.date, reverse=True)
        ordered_notes.sort(key=lambda note: (-note.user.is_professor(), -note.user.followers_count()))
        return list(ordered_notes)

    @classmethod
    def get_str_general_notes(cls, general_notes):
        notes = ""
        for note in general_notes:
            notes += note.content + ","
        return notes[:-1]
