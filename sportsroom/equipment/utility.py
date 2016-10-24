from datetime import timedelta

from django.utils import timezone


def get_due_date(days_allowed=7):
    return timezone.now() + timedelta(days_allowed)


table_tennis_racket = 'TTR'
shuttle_racket = 'SHR'
category_choices = (
    (table_tennis_racket, 'TT Racket'),
    (shuttle_racket, 'Shuttle Racket'),
)
