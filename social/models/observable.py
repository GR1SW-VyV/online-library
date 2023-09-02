from django.db import models


class Observable:
    followers = models.ManyToManyField('self')
    activities = []

    def is_followed_by(self, follower):
        pass

    def add_follower(self, observer):
        pass

    def add_activity(self, activity):
        self.activities.append(activity)
        self.notify()

    def notify(self):
        pass

    def followers_count(self):
        return self.followers.all().count()
