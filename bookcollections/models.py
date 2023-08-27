from django.db import models
from django.utils.translation import gettext_lazy as _


class MockArticle(models.Model):
    """
    Mocking model to handle dependencies with Article model
    """
    class Category(models.IntegerChoices):
        UNKNOWN = 0, _('Desconocido')


class Collection(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_public = models.BooleanField(default=False, null=False)

    category = models.CharField(
        max_length=100,
        choices=MockArticle.Category.choices,
        default=MockArticle.Category.UNKNOWN
    )

    def __str__(self):
        return self.name
