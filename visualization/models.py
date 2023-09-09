from django.db import models

from articles.models import Document
from social.models import User


class GeneralNote(models.Model):
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class PageNote(models.Model):
    content = models.TextField()
    date = models.DateField()
    is_favorite = models.BooleanField(default=False)
    page = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class PageNoteDAO:
    @classmethod
    def get_personal_page_notes(cls, username, book_id, page):
        notes = PageNote.objects.all().filter(user__username=username, document__uid=book_id, page=page)
        ordered_notes = list(notes)
        ordered_notes.sort(key=lambda note: (-note.is_favorite, note.date))
        return list(ordered_notes)

    @classmethod
    def get_page_notes(cls, username, book_id, page):
        notes = PageNote.objects.all().exclude(user__username=username).filter(document__uid=book_id, page=page)
        ordered_notes = list(notes)
        ordered_notes.sort(key=lambda note: (-note.user.is_professor(), -note.is_favorite, note.user.followers, note.date))
        return list(ordered_notes)


class GeneralNoteDAO:
    @classmethod
    def get_personal_general_notes(cls, username, book_id):
        notes = GeneralNote.objects.all().filter(user__username=username, document__uid=book_id)
        ordered_notes = list(notes)
        ordered_notes.sort(key=lambda note: note.date)
        return list(ordered_notes)

    @classmethod
    def get_general_notes(cls, username, book_id):
        notes = GeneralNote.objects.all().exclude(user__username=username).filter(document__uid=book_id)
        ordered_notes = list(notes)
        ordered_notes.sort(key=lambda note: (-note.user.is_professor(), note.user.followers, note.date))
        return list(ordered_notes)
