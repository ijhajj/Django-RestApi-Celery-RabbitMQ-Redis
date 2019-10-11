import time
import threading

def countdown(count):
    while(count>=0):
        print("'{0}' count down -> {1}".format(threading.current_thread().name, count))
        count -= 1
        time.sleep(3)
def countup():
    count=0
    while(count<=10):
        print("'{0}' count up -> {1}".format(threading.current_thread().name, count))
        count += 1
        time.sleep(5)

print(threading.__file__)
th1 = threading.Thread(target=countdown, args=(10,), name='thread1')
th2 = threading.Thread(target=countup, args=(), name='thread2')
th1.start()
th2.start()

#countdown(10)
print("All done!")
