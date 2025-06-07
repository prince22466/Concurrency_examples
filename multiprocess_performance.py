
#### Performance threading vs multiprocessing under cpu instense operations
# python version being used is python 3.13


import multiprocessing
from multiprocessing import Process,Queue
import time

def calculation(num,multi_queue):
    """computation intense"""
    """this func run in sequential and multithreads, wont make a diff"""
    multi_queue.put(sum(range(num)))



if __name__ == "__main__":

    print("all avialbe cores: ", multiprocessing.cpu_count())
    n_processes=4
    num_to_sum = 10**8
    queue=Queue()
    processes = []
    processes_current_t = time.time()
    for i in range(n_processes):
        p = Process(target=calculation, args=(num_to_sum*i,queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("All processes finished, took(sec): ", time.time()-processes_current_t)

    print("multi_queue size: ",queue.qsize())
    
    sum_queue=0
    while not queue.empty():
        val =queue.get()
        sum_queue += val
        print(val)

    print("sum of queue, ",sum_queue)

    print("All finished")
