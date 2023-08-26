from abc import ABC, abstractmethod


class Observable(ABC):
    followers = []
    activities = []

    def add_follower(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass
