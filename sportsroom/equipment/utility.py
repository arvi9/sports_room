from datetime import timedelta

from django.utils import timezone


def get_due_date(days_allowed=7):
    return timezone.now() + timedelta(days_allowed)


table_tennis_racket = 'TTR'
shuttle_racket = 'SHR'
shuttle_cock = 'SHC'
table_tennis_ball = 'TTB'
football = 'FTB'
cricket_ball = 'CBL'
cricket_bat = 'CBT'
category_choices = (
    (table_tennis_racket, 'TT Racket'),
    (table_tennis_ball, 'TT Ball'),
    (shuttle_racket, 'Shuttle Racket'),
    (shuttle_cock, 'Shuttlecock'),
    (football, 'Football'),
    (cricket_ball, 'Cricket Ball'),
    (cricket_bat, 'Cricket Bat'),
)
