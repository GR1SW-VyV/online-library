from social.models.activity import UserActivity
from social.models.observable import Observable
from social.models.observer import Observer
from social.models.collection import Collection


class User(Observer, Observable):
    name = ""
    followed_users = []
    followed_collections = []

    def notify(self):
        for observer in self.followers:
            observer.update(self.activities[-1])

    def update(self, activity):
        self.feed.append(activity)

    def do_activity(self):
        activity = self.create_user_activity("does a new activity")
        self.add_activity(activity)

    def create_user_activity(self, detail):
        activity = UserActivity()
        activity.observable = self
        activity.detail = detail
        return activity

    def follow(self, observable):
        super().follow(observable)
        if isinstance(observable, User):
            self.followed_users.append(observable)
        elif isinstance(observable, Collection):
            self.followed_collections.append(observable)

    def is_following(self, observable):
        return observable in self.followed_users

    def is_in_my_following_collection(self, collection):
        return collection in self.followed_collections
