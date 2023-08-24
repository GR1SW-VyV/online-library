import shutil

from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=60)
    subject = models.CharField(max_length=50)
    uid = models.CharField(max_length=50, primary_key=True)
