class Observer:
    feed = []

    def update(self, activity):
        pass

    def is_following(self, observable):
        pass

    def follow(self, observable):
        observable.add_follower(self)

    def in_my_feed(self, activity):
        return activity in self.feed.all()
