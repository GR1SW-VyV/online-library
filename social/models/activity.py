from datetime import datetime


class Activity:
    observable = None
    detail = ""
    date = datetime.today().date()

    def __eq__(self, other):
        if isinstance(other, Activity):
            return self.observable == other.observable and self.detail == other.detail and self.date == other.date
        return False

    def __hash__(self):
        return hash(self.observable) + hash(self.detail) + hash(self.date)


class CollectionActivity(Activity):
    document = None

    def __eq__(self, other):
        if isinstance(other, CollectionActivity):
            return super().__eq__(other) and self.document == other.document
        return False

    def __hash__(self):
        return super().__hash__() + hash(self.document)


class UserActivity(Activity):
    pass
