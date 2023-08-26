from social.models.observable import Observable
from social.models.observer import Observer
from social.models.collection import Collection


class User(Observer, Observable):
    name = ""
    followed_users = []
    followed_collections = []

    def notify(self):
        pass

    def update(self, activity):
        self.feed.append(activity)

    def do_activity(self):
        pass

    def follow(self, observable):
        super().follow(observable)
        if isinstance(observable, User):
            self.followed_users.append(observable)

    def is_following(self, observable):
        return observable in self.followed_users

    def is_in_my_following_collection(self, collection):
        pass
