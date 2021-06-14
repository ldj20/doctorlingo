y

import time
import multiprocessing as mp
from multiprocessing import Pool
print(mp.cpu_count())
 
def f(a_list):
    out = 0
    for n in a_list:
        out += n*n
        time.sleep(0.1)
 
    return out
 
def f_mp(a_list):
    chunks = [a_list[i::5] for i in range(5)]
 
    pool = Pool(processes=5)
 
    result = pool.map(f, chunks)
 
    return sum(result)



"""import time
import queue
import random
import multiprocessing as mp
from multiprocessing import Process


def calc_square(numbers):
    for i in numbers:
        time.sleep(3)  # artificial time-delay
        print('square: ', str(i * i))


def calc_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print('cube: ', str(i * i * i))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    # creating two Process here p1 & p2
    p1.start()
    p2.start()
    # starting Processes here parallel by using start function.
    p1.join()
    # this join() will wait until the calc_square() function is finished.
    p2.join()
    # this join() will wait unit the calc_cube() function is finished.
    print("Successes!")
"""
"""
    if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))
    # creating two threads here t1 & t2
    t1.start()
    t2.start()
    # starting threads here parallel by using start function.
    t1.join()
    # this join() will wait until the cal_square() function is finished.
    t2.join()
    # this join() will wait unit the cal_cube() function is finished.
    print("Successes!")
"""