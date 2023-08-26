import shutil
from django.utils.translation import gettext_lazy as _

from django.db import models


# Create your models here.


class Article(models.Model):
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

    title = models.CharField(max_length=120)
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.BOOK
    )
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
        default=Category.UNKNOWN
    )

    author = models.CharField(max_length=60)

    def url(self) -> str:
        return ""

    def reviews(self) -> list:
        return list()

    def notes(self) -> list:
        return list()
