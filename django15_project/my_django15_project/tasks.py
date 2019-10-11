from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@periodic_task(name='tasks.email_crontab_schedule', run_every=crontab(hour='*', minute='*', day_of_week=5))
def email_crontab_schedule():
    try:
        message_sent="email.example"
        print("Email is sent to the Worker[{}]".format(message_sent))
    finally:
        #Release all resources
        print("Resources Released")
