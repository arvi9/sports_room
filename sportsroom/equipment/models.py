from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import timedelta
from django.utils import timezone
from decimal import Decimal


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    fine = models.DecimalField(default=Decimal('0.00'), max_digits=7, decimal_places=2)

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, '_phone_number'):
            Student.objects.create(user=instance, phone_number=instance._phone_number)
        else:
            Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()


class Equipment(models.Model):
    TABLE_TENNIS_RACKET = 'TTR'
    SHUTTLE_RACKET = 'SHR'
    CATEGORY_CHOICES = (
        (TABLE_TENNIS_RACKET, 'TT Racket'),
        (SHUTTLE_RACKET, 'Shuttle Racket'),
    )
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES
    )
    n_equipment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.category


def get_duedate():
    return timezone.now() + timedelta(days=7)


class BorrowedItem(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=get_duedate)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.equipment.category


class Queue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    book_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        ordering = ['book_date']
