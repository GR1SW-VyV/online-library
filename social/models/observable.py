from abc import ABC, abstractmethod


class Observable(ABC):
    followers = []
    activities = []

    def in_my_feed(self, activity):
        pass

    def is_followed_by(self, follower):
        pass

    def add_follower(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass
