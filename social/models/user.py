from django.db import models

from social.models.activity import UserActivity
from social.models.collection import Collection
from social.models.observable import Observable
from social.models.observer import Observer


class User(Observer, Observable, models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    followed_users = []
    followed_collections = []
    feed = models.ManyToManyField('Activity')
    followers = models.ManyToManyField('User', symmetrical=False, blank=True, related_name='user_followers')

    def notify(self):
        for observer in self.followers.all():
            observer.update(self.activities[-1])

    def update(self, activity):
        print("-----------------" * 2)
        self.feed.add(activity)
        print(self.feed.all().count())

    def do_activity(self):
        activity = self.create_user_activity("does a new activity")
        activity.save()
        self.add_activity(activity)

    def create_user_activity(self, detail):
        activity = UserActivity()
        activity.responsible = self
        activity.detail = detail
        return activity

    def add_follower(self, observer):
        self.followers.add(observer)

    def follow(self, observable):
        super().follow(observable)
        if isinstance(observable, User):
            self.followed_users.append(observable)
        elif isinstance(observable, Collection):
            self.followed_collections.append(observable)

    def is_following(self, observable):
        return self in observable.followers.all()

    def is_in_my_following_collection(self, collection):
        return self in collection.followers.all()

    def is_followed_by(self, follower):
        return follower in self.followers.all()

    def following_users_count(self):
        return User.objects.filter(followers=self).count()

    def following_collections_count(self):
        return Collection.objects.filter(followers=self).count()
