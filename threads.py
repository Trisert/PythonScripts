from threading import Thread
import os
import math 


def calc():
    for i in range(0, 900000):
        print(math.sqrt(i))

threads = []

for i in range(os.cpu_count()):
    print('registering thread %d' % i)
    threads.append(Thread(target=calc))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
