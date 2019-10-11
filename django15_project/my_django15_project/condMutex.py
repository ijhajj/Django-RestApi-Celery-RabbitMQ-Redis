import threading
import time
import random

queue = []
MAX_ITEMS = 10
condition = threading.Condition()

class Producer_class(threading.Thread):
    """ Creating a produce class by extending thread class """
    def run(self):
        """ override the run function """
        numbers = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_ITEMS:
                print("Queue is Full, producer is in Waiting state")
                condition.wait() # This actually releases the lock and notifies other threads waiting on it - consumer in this case
            # if queue has space
            print("Space in Queue, Producer is adding numbers to queue")
            number = random.choice(numbers)
            queue.append(number)
            print("Produced {}".format(number))
            condition.notify()
            condition.release()
            time.sleep(random.random())

class Consumer_class(threading.Thread):
    """ Creating consumer class to consume the numbers """
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait()
            print("Producer added numbers, consumer resuming")
            number = queue.pop(0)
            print("Consumer {}".format(number))
            condition.notify() #notifies producer to resume, it does not actually release the lock
            condition.release()
            time.sleep(random.random())

#both the consumer and producer share the same condition which is turned ON/OFF
producer = Producer_class()
producer.daemon = True
producer.start()

consumer = Consumer_class()
consumer.daemon = True
consumer.start()

while True:
    time.sleep(1)
