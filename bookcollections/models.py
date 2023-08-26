from django.db import models
from articles.models import Article

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_public = models.BooleanField(default=False, null=False)

    category = models.CharField(
        max_length=100,
        choices=Article.Category.choices,
        default=Article.Category.UNKNOWN
    )

    def __str__(self):
        return self.name
