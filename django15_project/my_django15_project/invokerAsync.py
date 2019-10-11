from tasks import add
from celery.result import AsyncResult
import time

""" illustrating an asynchronous task that takes a long time to process """
""" We can keep checking its status and fetch the results once completed """
result = add.delay(1, 5)

while True:
    _result2 = AsyncResult(result.task_id)
    #print(_result2)
    status = _result2.status
    #print('Here is the status {}'.format(_result2.state))
    print(status)
    if 'SUCCESS' in status:
        print('result after 5 sec wait {result2}'.format(result2=_result2.get()))
        break
    time.sleep(5)
