from multiprocessing import Pool
from time import perf_counter

def squares(number):
    for i in range(10000):
        number = number * i
    return number

if __name__=="__main__":
    LENGTH = 1000000
    pool = Pool()
    starttime = perf_counter()
    results = pool.map(squares,range(LENGTH))
    endtime = perf_counter()
    print(f"time takes about {endtime - starttime}")
    
    starttime = perf_counter()
    for i in range(LENGTH):
        squares(i)
    endtime = perf_counter()
    print(f"time takes about {endtime - starttime}")
    
