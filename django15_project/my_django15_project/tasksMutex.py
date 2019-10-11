from celery import Celery
import time
from celery.decorators import periodic_task
from datetime import timedelta
#import redis to implement the mutually exclusive logic so our multiple workers do not fall into a race condition
import redis

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

key = '4088587A2CAB44FD902D6D5C98CD2B17'
#self is used so as to bind it with 'bind=True' ensuring we can use the instance data of the worker
#executing this asynchronous task
@periodic_task(bind=True, run_every=timedelta(seconds=5), name='tasks.send_mail_from_queue')
def send_email_from_queue(self):
    """ ensuring in case of multiple workers running, tasks are picked up in a
    mutually exclusive manner to avoid duplicate tasks """
    REDIS_CLIENT = redis.Redis()
    timeout = 60 * 5    #lock expires in 5 min
    have_lock = False
    my_lock = REDIS_CLIENT.lock(key, timeout=timeout)
    try:
        have_lock = my_lock.acquire(blocking=False)
        if have_lock:
            message_sent="example.email"
            #self.request.hostname will contain the name of the worker executing this task
            print("{} Email being sent successfully [{}]".format(self.request.hostname, message_sent))
            time.sleep(10)
    finally:
        print("Resources are released")
        if have_lock:
            my_lock.release()
