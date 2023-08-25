from abc import ABC, abstractmethod
from typing import List
from social.models.activity import Activity
from social.models.observer import Observer


class Observable(ABC):
    followers: List[Observer] = []
    activities: List[Activity] = []

    def addFollower(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass
