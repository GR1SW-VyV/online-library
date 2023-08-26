from abc import ABC, abstractmethod


class Observer(ABC):
    feed = []

    @abstractmethod
    def update(self, activity):
        pass

    @abstractmethod
    def is_following(self, observable):
        pass

    def follow(self, observable):
        observable.add_follower(self)

    def in_my_feed(self, activity):
        return activity in self.feed
