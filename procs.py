from multiprocessing import Process 
import os
import math 


def calc():
    for i in range(0, 123456789):
        if math.sqrt(i) % 2 == 0:
            print('La radice di %s = %s' % (i, math.sqrt(i)))

processes = []

for i in range(os.cpu_count()):
    processes.append(Process(target=calc))

for process in processes:
    process.start()

for process in processes:
    process.join()
