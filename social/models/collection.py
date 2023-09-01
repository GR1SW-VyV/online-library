from django.db import models

from social.models.activity import CollectionActivity
from social.models.observable import Observable


class Collection(Observable, models.Model):
    name = models.CharField(max_length=20)
    followers = models.ManyToManyField('User', symmetrical=False, blank=True)

    def add_document(self, document):
        document.collections.add(self)
        activity = self.create_collection_activity(document)
        activity.save()
        self.add_activity(activity)

    def add_follower(self, observer):
        self.followers.add(observer)

    def create_collection_activity(self, document):
        activity = CollectionActivity()
        activity.collection = self
        activity.document = document
        activity.detail = "add a new document"
        return activity

    def notify(self):
        for follower in self.followers.all():
            follower.update(self.activities[-1])
