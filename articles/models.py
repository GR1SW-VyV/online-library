import shutil
import hashlib
from django.utils.translation import gettext_lazy as _
from bookcollections.models import Collection
from django.db import models
from .choices.category import Category

from . import services


# Create your models here.

class Document: ...
class Author:...


class Author(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_by_prefix(prefix:str):
        return Author.objects.filter(name__contains=prefix)


class Document(models.Model):
    class Type(models.TextChoices):
        BOOK = "BOOK", _('BOOK')
        ARTICLE = "ARTICLE", _('ARTICLE')

    uid = models.AutoField(primary_key=True)

    sha512 = models.CharField(max_length=128, default="")
    filename = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=120)
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.BOOK
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.UNKNOWN
    )
    author = models.ManyToManyField(Author)
    view_count = models.IntegerField(null=False, default=0)
    collections = models.ManyToManyField(Collection, related_name='books')
    score = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    def increase_view_count(self, count=1):
        self.view_count += 1
        self.save()

    def url(self) -> str:
        return f"/articles/resources/{self.category}/{self.filename}"

    @staticmethod
    def find_colliding_document(local_path) -> Document:
        file = open(local_path, "rb")
        sha512 = hashlib.sha512(file.read()).hexdigest()
        return Document.objects.filter(sha512=sha512).first()