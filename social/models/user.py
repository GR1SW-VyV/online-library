from social.models.observable import Observable
from social.models.activity import Activity
from social.models.observer import Observer
from social.models.collection import Collection
from typing import List


class User(Observer, Observable):
    name = ""
    followed_users: List['User'] = []
    followed_collections: List[Collection] = []

    def notify(self):
        pass

    def update(self, activity: Activity):
        pass

    def do_activity(self):
        pass
