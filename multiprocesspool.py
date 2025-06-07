
#### Performance threading vs multiprocessing under cpu instense operations
# python version being used is python 3.13


import multiprocessing
from multiprocessing import Pool
import time

def calculation_multiparams(num1,num2):
    """computation intense"""
    """this func run in sequential and multithreads, wont make a diff"""
    return sum(range(num1,num2))

def calculation_singleparams(num1):
    """computation intense"""
    """this func run in sequential and multithreads, wont make a diff"""
    return sum(range(num1))


if __name__ == "__main__":

    print("all avialbe cores: ", multiprocessing.cpu_count())
    n_processes=4
    nums_1 = [10**8 , 24, 40]
    nums_2 = [10**8*2 , 24*3, 40*3]

    with Pool(n_processes) as pool:
        result_singleparam = pool.map(calculation_singleparams, nums_1)#map can only take one parameter 
        result_multiparam = pool.starmap(calculation_multiparams, zip(nums_1,nums_2))


    print("result_singleparam, ",result_singleparam)
    print("result_multiparam, ",result_multiparam  )

    print("All finished")
