from datetime import timedelta

from django.utils import timezone


def get_due_date(days_allowed=7):
    return timezone.now() + timedelta(days=7)
