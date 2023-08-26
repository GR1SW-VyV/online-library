from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, activity):
        pass

    def follow(self, observable):
        pass
