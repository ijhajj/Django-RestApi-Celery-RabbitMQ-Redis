from celery import Celery

#Define Celery module
#backend points to where the results are stored like rabbitMQ, DB etc
#currently we have it as none, but if we invoke the add function and instead of returning the result
# return the value in a variable, that would be termed as backend
app = Celery('tasks', backend=None, broker='redis://localhost:6379/0')

#define the decorator along with function that needs to be converted into a Celery task
#CeleryModule.task(taskname)
@app.task(name='tasks.add')
def add(x,y):
    print('{} + {} = {}'.format(x,y,(x+y)))
