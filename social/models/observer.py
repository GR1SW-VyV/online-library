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
        pass

