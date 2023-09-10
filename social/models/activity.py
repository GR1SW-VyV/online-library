from datetime import datetime
from django.db import models
from polymorphic.models import PolymorphicModel


class Activity(PolymorphicModel):
    detail = models.CharField(max_length=100)
    date = models.DateField(default=datetime.today)
    time = models.TimeField(default=datetime.now().time())

    def __eq__(self, other):
        if isinstance(other, Activity):
            return self.detail == other.detail and self.date == other.date
        return False

    def __hash__(self):
        return hash(self.detail) + hash(self.date)


class CollectionActivity(Activity):
    document = models.ForeignKey('articles.Document', on_delete=models.CASCADE)
    collection = models.ForeignKey('bookcollections.Collection', on_delete=models.CASCADE)

    def __eq__(self, other):
        if isinstance(other, CollectionActivity):
            return super().__eq__(other) and self.document == other.document and self.collection == other.collection
        return False

    def __hash__(self):
        return super().__hash__() + hash(self.collection) + hash(self.document)


class UserActivity(Activity):
    responsible = models.ForeignKey('social.User', on_delete=models.CASCADE)
    collection = models.ForeignKey('bookcollections.Collection', on_delete=models.CASCADE, null=True, blank=True)

    def __eq__(self, other):
        if isinstance(other, UserActivity):
            return super().__eq__(other) and self.responsible == other.responsible
        return False

    def __hash__(self):
        return super().__hash__() + hash(self.responsible)
