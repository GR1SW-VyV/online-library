from abc import ABC, abstractmethod


class Observable(ABC):
    followers = []
    activities = []

    def is_followed_by(self, follower):
        return follower in self.followers

    def add_follower(self, observer):
        self.followers.append(observer)

    def add_activity(self, activity):
        self.activities.append(activity)
        self.notify()

    @abstractmethod
    def notify(self):
        pass
