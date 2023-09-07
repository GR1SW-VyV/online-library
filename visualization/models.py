from django.db import models
from social.models import User
from articles.models import Document


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
    def get_personal_page_notes(cls, username, document_id, page):
        notes = PageNote.objects.all().filter(user__username=username, document__uid=document_id, page=page)
        ordered_notes = cls.order_notes(notes)
        return list(ordered_notes)

    @classmethod
    def get_page_notes(cls, username, document_id, page):
        notes = PageNote.objects.all().exclude(user__username=username).filter(document__uid=document_id, page=page)
        ordered_notes = cls.order_notes(notes)
        return list(ordered_notes)

    @classmethod
    def order_notes(cls, notes):
        ordered_notes = sorted(notes, key=lambda note: note.user.is_professor(), reverse=True)
        ordered_notes = sorted(ordered_notes, key=lambda note: note.is_favorite, reverse=True)
        ordered_notes = sorted(ordered_notes, key=lambda note: note.user.followers.count())
        ordered_notes = sorted(ordered_notes, key=lambda note: note.date)
        return ordered_notes


class GeneralNoteDAO:
    @classmethod
    def get_personal_general_notes(cls, username, document_id):
        notes = GeneralNote.objects.all().filter(user__username=username, document__uid=document_id)
        ordered_notes = cls.order_notes(notes)
        return list(ordered_notes)

    @classmethod
    def get_general_notes(cls, username, document_id):
        notes = GeneralNote.objects.all().exclude(user__username=username).filter(document__uid=document_id)
        ordered_notes = cls.order_notes(notes)
        return list(ordered_notes)

    @classmethod
    def order_notes(cls, notes):
        ordered_notes = sorted(notes, key=lambda note: note.user.is_professor(), reverse=True)
        ordered_notes = sorted(ordered_notes, key=lambda note: note.user.followers.count())
        ordered_notes = sorted(ordered_notes, key=lambda note: note.date)
        return ordered_notes
