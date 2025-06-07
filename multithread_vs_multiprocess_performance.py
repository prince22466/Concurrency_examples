
#### Performance threading vs multiprocessing under cpu instense operations
# python version being used is python 3.13

import threading
import multiprocessing
from multiprocessing import Process
import time

def calculation(num):
    """computation intense"""
    """this func run in sequential and multithreads, wont make a diff"""
    sum(range(num))



if __name__ == "__main__":

    print("all avialbe cores: ", multiprocessing.cpu_count())
    n_threads=4
    n_processes=4
    num_to_sum = 10**8

    threads = []
    thread_current_t = time.time()
    for _ in range(n_threads):
        t = threading.Thread(target=calculation, args=(num_to_sum,))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    print("All threads finished, took(sec): ", time.time()-thread_current_t)


    processes = []
    processes_current_t = time.time()
    for _ in range(n_processes):
        p = Process(target=calculation, args=(num_to_sum,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("All processes finished, took(sec): ", time.time()-processes_current_t)


    print("All finished")
