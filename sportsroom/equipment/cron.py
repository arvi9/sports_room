from datetime import datetime, timezone

from django.core.mail import send_mail
from django_cron import CronJobBase, Schedule

from .models import BorrowedItem, Student, Queue, SportsRoomConstants

class UpdateFineCronJob(CronJobBase):
    RUN_EVERY_MINS = 120  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'equipment.update_fine_cron_job'  # a unique code

    def do(self):
        print("running update cron")  # do your thing here
        items = BorrowedItem.objects.all()
        fine = int(SportsRoomConstants.objects.get(key="fine"))

        for item in items:
            diff = item.return_date - item.due_date
            print(diff.days)
            #TODO: Extract calculate_fine logic
            if diff.days > 0:
                s = Student.objects.get(id=item.student.id)
                s.fine += fine
                email = s.user.email
                email_content = 'You have a fine of Rs.' + s.fine + ' due! Make sure you pay it as soon as possible.'
                s.save()

                print(email)
                # TODO: Cleanup
                send_mail(
                    'Fine Due',
                    email_content,
                    to=[email],
                    fail_silently=False,
                )


class ResetQCronJob(CronJobBase):
    RUN_EVERY_MINS = 120  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'equipment.reset_q_cron_job'  # a unique code

    def do(self):
        print( "running reset Queue cron") # do your thing here
        students = Queue.objects.all()
        now = datetime.now(timezone.utc)
        for student in students:
            date = student.book_date
            # print(date)
            #TODO: Cleanup
            if (now - date).days >= 3:
                Queue.objects.filter(id=student.id).delete()
