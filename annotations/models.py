from django.db import models
from social.models.user import User
from articles.models import Document


# Create your models here.
class PageNote(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    page = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class PageNoteDAO:
    @classmethod
    def get_notes_by_page(cls, user_id, document_id, page):
        """
            :param user_id: ID del usuario.
            :param document_id: ID del documento.
            :param page: Número de página.
            :return: Lista de notas de la página especificada.
        """
        return PageNote.objects.filter(user_id=user_id, document_id=document_id, page=page)

    @classmethod
    def get_all_notes_of_document(cls, user_id, document_id):
        """
            :param user_id: ID del usuario.
            :param document_id: ID del documento.
            :return: Lista de todas las notas del documento.
        """
        return PageNote.objects.filter(user_id=user_id, document_id=document_id)

    @classmethod
    def mark_note_as_favorite(cls, note_id):
        note = PageNote.objects.get(pk=note_id)
        note.is_favorite = True
        note.save()

    @classmethod
    def get_note_by_id(cls, note_id):
        return PageNote.objects.get(pk=note_id)
