from django.db import models
from social.models.user import User


# Create your models here.
class Note(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # document = models.ForeignKey(Document, on_delete=models.CASCADE)


class MockDocument(models.Model):
    """
    Mocking model to handle dependencies with Document model
    """


class NoteDAO:
    @classmethod
    def get_notes_by_page(cls, user_id, document_id, page):
        """
            :param user_id: ID del usuario.
            :param document_id: ID del documento.
            :param page: Número de página.
            :return: Lista de notas de la página especificada.
        """
        return Note.objects.filter(user_id=user_id, document_id=document_id, page=page)

    @classmethod
    def get_all_notes_of_document(cls, user_id, document_id):
        """
            :param user_id: ID del usuario.
            :param document_id: ID del documento.
            :return: Lista de todas las notas del documento.
        """
        return Note.objects.filter(user_id=user_id, document_id=document_id)
