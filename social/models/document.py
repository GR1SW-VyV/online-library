from django.db import models

from social.models.collection import Collection


class Document(models.Model):
    title = models.CharField(max_length=30)
    collections = models.ManyToManyField(Collection, related_name='books')
