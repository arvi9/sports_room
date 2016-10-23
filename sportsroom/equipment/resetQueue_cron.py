




from datetime import datetime, timedelta, timezone
from . import models
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'equipment.my_cron_job'    # a unique code

    def do(self):
        #print( "running reset Queue cron") # do your thing here
        profiles = models.Queue.objects.all()
        now = datetime.now(timezone.utc)
        #print(now)
        for profile in profiles:
            date = profile.book_date
            #print(date)
            if ((now - date).days >= 3):
                models.Queue.objects.filter(id=profile.id).delete()

