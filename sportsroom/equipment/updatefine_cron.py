from . import models
from django.core.mail import send_mail
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'equipment.my_cron_job'    # a unique code

    def do(self):
        print( "running update cron") # do your thing here
        profiles = models.BorrowedItem.objects.all()

        for profile in profiles:
            #print(profile.due_date)
            #print(profile.return_date)
            dt = (profile.return_date - profile.due_date)
            print(dt.days)
            if(dt.days > 0):
                #id = profile.id
                #print(id)
                t = models.Student.objects.get(id=profile.id)
                t.fine+=10
                email = t.user.email
                t.save()


                print(email)
                send_mail(
                    'Fine Due',
                    'You have some fine due! Make sure you pay it as soon as possible.',
                    'sports.room.iiitb@gmail.com',
                    [email],
                    fail_silently=False,
                )