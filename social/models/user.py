from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.contenttypes.models import ContentType
from social.models.activity import UserActivity
from social.models.collection import Collection
from social.models.observable import Observable
from social.models.observer import Observer
from ..constants import *


def create_user(user, group_names=(), permissions=()):
    user = User.objects.create_user(
        username=user.username,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )

    if isinstance(group_names, str):
        group_names = (group_names,)

    for group_name in group_names:
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

    content_type = ContentType.objects.get_for_model(User)

    for permission in permissions:
        permission, _ = Permission.objects.get_or_create(
            codename=permission,
            content_type=content_type
        )
        user.user_permissions.add(permission)

    return user


def create_reader_user(user):
    return create_user(user, READER_GROUP, [CAN_NOTE_PERMISSION,
                                            CAN_READ_PERMISSION,
                                            CAN_CREATE_COLLECTION_PERMISSION])


def create_professor_user(user):
    return create_user(user, PROFESSOR_GROUP, [CAN_NOTE_PERMISSION,
                                               CAN_READ_PERMISSION,
                                               CAN_CREATE_COLLECTION_PERMISSION,
                                               CAN_PUBLISH_PERMISSION])


class User(Observer, Observable, AbstractUser):
    feed = models.ManyToManyField('Activity')
    followers = models.ManyToManyField('User', symmetrical=False, blank=True, related_name='user_following')

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
        return Collection.objects.filter(followers=self).count()

    def is_reader(self):
        return self.groups.filter(name='Reader').exists()

    def is_professor(self):
        return self.groups.filter(name='Professor').exists()
