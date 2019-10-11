import threading

counter_buffer = 0
counter_lock = threading.Lock()

COUNTER_MAX = 100
THREAD_COUNT = 5

def consumer1_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        #counter_lock.acquire()
        counter_buffer +=1
        #counter_lock.release()

def consumer2_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        counter_lock.acquire()
        counter_buffer +=1
        counter_lock.release()

threadList=[]
for i in range(THREAD_COUNT):
    th = threading.Thread(target=consumer1_counter, args=(), name='thread')
    threadList.append(th)
#th2 = threading.Thread(target=consumer2_counter, args=(), name='consumer1')

for threads in threadList:
    threads.start()
    threads.join()

#th1.start()
#th2.start()

#th1.join()
#th2.join()

print(counter_buffer)
