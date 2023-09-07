from django.db import models
from django.contrib.auth.models import AbstractUser
from social.models.activity import UserActivity
from social.models.observable import Observable
from social.models.observer import Observer
from social.models.user_manager import UserManager


class User(Observer, Observable, AbstractUser):
    feed = models.ManyToManyField('Activity')
    followers = models.ManyToManyField('User', symmetrical=False, blank=True, related_name='user_following')
    objects = UserManager()

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

    def log_collection_creation(self, collection):
        activity = self.create_user_activity("created a new collection", collection)
        activity.save()
        self.add_activity(activity)

    def create_user_activity(self, detail, collection=None):
        activity = UserActivity()
        activity.responsible = self
        activity.collection = collection
        activity.detail = detail
        return activity

    def add_follower(self, observer):
        self.followers.add(observer)

    def follow(self, observable):
        super().follow(observable)

    def is_following(self, observable):
        return self in observable.followers.all()

    def is_in_my_following_collection(self, collection):
        return self in collection.followers.all()

    def is_followed_by(self, follower):
        return follower in self.followers.all()

    def following_users_count(self):
        return User.objects.filter(followers=self).count()

    def following_collections_count(self):
        from bookcollections.models import Collection
        return Collection.objects.filter(followers=self).count()

    def is_reader(self):
        return self.groups.filter(name='Reader').exists()

    def is_professor(self):
        return self.groups.filter(name='Professor').exists()
