from datetime import datetime
from django.db import models
from polymorphic.models import PolymorphicModel


class Activity(PolymorphicModel):
    detail = models.CharField(max_length=100)
    date = models.DateField(default=datetime.today)
    time = models.TimeField(default=datetime.now().time())


class CollectionActivity(Activity):
    document = models.ForeignKey('articles.Document', on_delete=models.CASCADE)
    collection = models.ForeignKey('bookcollections.Collection', on_delete=models.CASCADE)


class UserActivity(Activity):
    responsible = models.ForeignKey('social.User', on_delete=models.CASCADE)
    collection = models.ForeignKey('bookcollections.Collection', on_delete=models.CASCADE, null=True, blank=True)
