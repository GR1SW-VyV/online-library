import hashlib
import shutil
from django.utils.translation import gettext_lazy as _

from django.db import models

from . import services
# Create your models here.


class Document(models.Model):
    class Category(models.TextChoices):
        UNKNOWN = "UNKNOWN", _('UNKNOWN')
        MATH = "MATH", _('MATH')
        PHYSICS = "PHYSICS", _('PHYSICS')
        CALCULUS = "CALCULUS", _('CALCULUS')
        PROGRAMMING = "PROGRAMMING", _('PROGRAMMING')
        LITERATURE = "LITERATURE", _('LITERATURE')
        ECONOMY = "ECONOMY", _('ECONOMY')
        GEOMETRY = "GEOMETRY", _('GEOMETRY')
        CHEMISTRY = "CHEMISTRY", _('CHEMISTRY')

    class Type(models.TextChoices):
        BOOK = "BOOK", _('BOOK')
        ARTICLE = "ARTICLE", _('ARTICLE')

    uid = models.CharField(max_length=50, primary_key=True)

    sha512 = models.CharField(max_length=128, default="")

    filename = models.CharField(max_length=200,null=True)
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

    author = models.CharField(max_length=60)

    view_count = models.IntegerField(null=False, default=0)

    def increase_view_count(self, count=1):
        self.view_count += 1
        self.save()

    def url(self) -> str:
        return f"/articles/resources/{self.category}/{self.filename}"

    def collections(self) -> list[models.Model]:
        return list()

    def reviews(self) -> list[models.Model]:
        return list()

    def notes(self) -> list[models.Model]:
        return list()

    @staticmethod
    def check_existence(local_path):
        file = open(local_path, "rb")
        sha512 = hashlib.sha512(file.readlines())
        Mode
