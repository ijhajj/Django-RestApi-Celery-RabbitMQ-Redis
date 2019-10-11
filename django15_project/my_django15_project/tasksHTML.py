from celery import Celery
import time

app=Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@app.task(name='tasks.add')
def add(x,y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total ))
    time.sleep(10)
    return total


def backoff(attempts):
    """ for each attempt it backs off a little bit and attempts again SMARTLY """
    return 2 ** attempts


@app.task(bind=True,max_retries=4, soft_time_limit=5)
def data_extractor(self):
    try:
        for i in range(1,10):
            print('Crawling HTML DOM!')
            if i == 5:
                raise ValueError('Crawling Index Error')
    except Exception as exc:
        print('Exception lets try in 5 sec')
        #raise self.retry(exc=exc, countdown=5 )
        raise self.retry(exc=exc, countdown=backoff(self.request.retries))
