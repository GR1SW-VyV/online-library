from django import template
from social.models import UserActivity, CollectionActivity
from datetime import datetime


register = template.Library()


@register.filter(name='is_collection_activity')
def is_collection_activity(activity):
    return isinstance(activity, CollectionActivity)


@register.filter(name='is_user_activity')
def is_user_activity(activity):
    return isinstance(activity, UserActivity)


@register.filter(name='format_counter')
def format_counter(value):
    units = ['', 'k', 'M', 'B']
    exponent = 0
    while value >= 1000:
        value /= 1000
        exponent += 1
    formatted_value = f"{value:.1f}"
    if exponent == 0:
        formatted_value = str(value)
    return f"{formatted_value}{units[exponent]}"


@register.filter(name='time_since')
def time_since(value_date, value_time):
    now = datetime.now()
    value_datetime = datetime.combine(value_date, value_time)
    delta = now - value_datetime
    total_seconds = delta.total_seconds()

    if total_seconds < 60:
        return f'{int(total_seconds)} segundo{"s" if int(total_seconds) != 1 else ""}'
    elif total_seconds < 3600:
        minutes = int(total_seconds) // 60
        return f'{minutes} minuto{"s" if minutes != 1 else ""}'
    elif total_seconds < 86400:
        hours = int(total_seconds) // 3600
        return f'{hours} hora{"s" if hours != 1 else ""}'
    elif delta.days < 7:
        days = delta.days
        return f'{days} día{"s" if days != 1 else ""}'
    elif delta.days < 30:
        weeks = delta.days // 7
        return f'{weeks} semana{"s" if weeks != 1 else ""}'
    elif delta.days < 365:
        months = delta.days // 30
        return f'{months} mes{"es" if months != 1 else ""}'
    else:
        years = delta.days // 365
        return f'{years} año{"s" if years != 1 else ""}'
