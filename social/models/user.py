from social.models.observable import Observable
from social.models.observer import Observer


class User(Observer, Observable):
    name = ""
    followed_users = []
    followed_collections = []

    def notify(self):
        pass

    def update(self, activity):
        pass

    def do_activity(self):
        pass
