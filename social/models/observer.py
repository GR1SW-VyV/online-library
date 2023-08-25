from abc import ABC, abstractmethod
from social.models.observable import Observable

from social.models.activity import Activity


class Observer(ABC):
    @abstractmethod
    def update(self, activity: Activity):
        pass

    def follow(self, observable: Observable):
        pass
