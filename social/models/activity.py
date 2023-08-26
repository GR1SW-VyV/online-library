from datetime import datetime


class Activity:
    observable = None
    detail = ""
    date = datetime.today().date()


class CollectionActivity(Activity):
    document = None
