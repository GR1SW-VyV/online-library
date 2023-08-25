from social.models.observable import Observable
from datetime import datetime


class Activity:
    observable: Observable
    detail = ""
    date = datetime.date()
