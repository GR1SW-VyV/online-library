import os
import shutil

from django.db.models import Avg
import hashlib
from django.utils.translation import gettext_lazy as _
from django.db import models
from .choices.category import Category

from . import services


# Create your models here.

class Document: ...
class Author:...
class Score:...



class Author(models.Model):
    name = models.CharField(max_length=50,primary_key=True)

    @staticmethod
    def find_or_create(name):
        if name is None: return None
        author = Author.objects.filter(name=name).first()
        if author is not None: return author
        author = Author(name)
        author.save()
        return author

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
    author = models.OneToOneField(Author,on_delete=models.DO_NOTHING,null=True)
    view_count = models.IntegerField(null=False, default=0)
    collections = models.ManyToManyField('bookcollections.Collection', related_name='books')

    def increase_view_count(self, count=1):
        self.view_count += 1
        self.save()

    def local_path(self) -> str:
        return f"articles/resources/{self.category.capitalize()}Resources/{self.filename}"

    def url(self) -> str:
        category_str = str(self.category).capitalize()
        return f"/static/articles/resources/{category_str}Resources/{self.filename}"

    def add_score(self, user_id, score):
        old_score = Score.objects.filter(user=user_id,document=self).first()
        if old_score is None:
            Score(user=user_id,document=self,value=score).save()
            return
        old_score.value = score
        old_score.save()

    def scores(self):
        return Score.objects.filter(document=self)


    def score(self):
        scores = self.scores()
        if scores.first() is None:
            return 0
        return scores.aggregate(Avg("value"))["value__avg"]

    @staticmethod
    def find_colliding_document(local_path) -> Document:
        file = open(local_path, "rb")
        sha512 = hashlib.sha512(file.read()).hexdigest()
        return Document.objects.filter(sha512=sha512).first()

    @staticmethod
    def from_local_path(path: str, /, author=None, category=Category.UNKNOWN, **kwargs) -> Document:
        category_str = str(category).capitalize()
        os.makedirs(f'./articles/resources/{category_str}Resources', exist_ok=True)
        shutil.copy(path, f'./articles/resources/{category_str}Resources/')


        file = open(path, "rb")
        sha512 = hashlib.sha512(file.read()).hexdigest()
        filename = path.split("/")[-1]

        document = Document(
            filename=filename,
            sha512=sha512,
            author=Author.find_or_create(author),
            category=category, **kwargs)
        document.save()
        return document


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.BigIntegerField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    value = models.FloatField()
