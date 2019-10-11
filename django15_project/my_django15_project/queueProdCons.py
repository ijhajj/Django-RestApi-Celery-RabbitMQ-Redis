import threading
import time
import queue
import random

_queue = queue.Queue(10)#declared a Queue with max size of 10
# As inbuilt queue DataStructures is used all conditional checks will no longer be required
#MAX_ITEMS = 10

#condition = threading.Condition()

class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(5)
        global _queue

        while True:
            #condition.acquire()
            #if len(_queue) == MAX_ITEMS:
            #    print("Queue is full.... Producer is waiting")
            #    condition.wait()
            #print("There is space in Queue.... Producer is producing")
            number = random.choice(numbers)
            #_queue.append(number)
            _queue.put(number)
            print("Produced {}".format(number))
            #condition.notify()
            #condition.release()
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def run(self):
        global _queue
        while True:
            #condition.acquire()
            #if not _queue:
            #    condition.acquire()
            #    print("Nothing in Queue... Consumer Waiting")
            #    condition.wait()
            #number = _queue.pop(0)
            number = _queue.get() #inherently fetches the first item on the top of the queue
            _queue.task_done() #Exclusively tell the queue that we extracted a number
            print("Consumed {}".format(number))
            #condition.notify()
            #condition.release()
            time.sleep(random.random())

producer = ProducerThread()
producer.start()

consumer = ConsumerThread()
consumer.start()
