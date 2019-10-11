from celery import Celery
import time
from celery.decorators import periodic_task
from datetime import timedelta

app=Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@periodic_task(run_every=timedelta(seconds=3), name="tasks.send_email_from_queue")
def send_mail_from_queue():
    """ periodic scheduling of a simple task using celery beat """
    try:
        message_sent = "example.email"
        print("Email message successfully sent, [{}]".format(message_sent))
    finally:
        print("Release Resources")
