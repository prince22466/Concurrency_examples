
#### Performance improvement with threading
# This code compares the performance of sequential execution and multithreading for two types of functions:
# 1. Computation-intensive function (calculation)
# 2. Non-computation-intensive function (sleep)
# multithreading is used to improve the performance of non-computation-intensive functions, 
# while it not the case for the performance of computation-intensive functions due to Python's Global Interpreter Lock (GIL).
# python version being used is python 3.13

import threading
import time

def calculation(num):
    """computation intense"""
    """this func run in sequential and multithreads, wont make a diff"""
    sum(range(num))


def sleep(sec):
    """non-computation intense, such as network server, route, the flow is on-off from time to time"""
    """this func run in sequential and multithreads, make a obvious diff"""
    time.sleep(sec)

if __name__ == "__main__":


    current_t = time.time()
    threads = []
    for i in range(5):
        num_to_sum = i*10000000
        t = threading.Thread(target=calculation, args=(num_to_sum,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads in 1st part  finished, took(sec): ", time.time()-current_t)


    current_t = time.time()
    threads = []
    for i in range(5):
        sec_sleep = i+1
        t = threading.Thread(target=sleep, args=(sec_sleep,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("All threads in 2nd part  finished, took(sec): ", time.time()-current_t)


    current_t = time.time()
    for i in range(5):
        num_to_sum = i*10000000
        calculation(num_to_sum)
    print("sequential run in 1st part  finished, took(sec): ", time.time()-current_t)


    current_t = time.time()
    for i in range(5):
        sec_sleep = i+1
        sleep(sec_sleep)

    print("sequential run in 2nd part  finished, took(sec): ", time.time()-current_t)


    print("All finished")
