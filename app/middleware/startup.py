from django.core.exceptions import MiddlewareNotUsed, ValidationError
from django.conf import settings
from django.utils import timezone
from django.core.management import call_command
from django_celery_beat.models import PeriodicTask, IntervalSchedule

#Startup Middleware for intializing periodic task(s)
# you still need to run celery beat service
# this only inserts the task and schedule into database

class StartupMiddleware(object):
    def __init__(self, _):
        schedule, _ = IntervalSchedule.objects.get_or_create(every=settings.C_PERIODIC_TASK_INTERVAL, period=settings.C_PERIODIC_TASK_TIMEUNIT)
        try:
            PeriodicTask.objects.create(interval=schedule,
                name=settings.SCRAPER_TASKNAME,
                task='scraper',
                queue=settings.SCRAPER_QUEUENAME,
                start_time=timezone.now()
                )
            print('task inserted')
        except ValidationError as err:
            print(repr(err))
        
        raise MiddlewareNotUsed('scraper started')