from django import template
from social.models import UserActivity, CollectionActivity

register = template.Library()


@register.filter(name='is_collection_activity')
def is_collection_activity(activity):
    return isinstance(activity, CollectionActivity)


@register.filter(name='is_user_activity')
def is_user_activity(activity):
    return isinstance(activity, UserActivity)
