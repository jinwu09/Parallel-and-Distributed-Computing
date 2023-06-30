from time import perf_counter, sleep
from threading import Thread
import concurrent.futures
from multiprocessing import Process, Pipe

def sumRange(start:int,end:int):
    sum = 0
    for i in range(start, end+ 1):
        # tempSum= sum +i
        # print(f'|{msg} {sum} + {i} = {tempSum} |')
        # sum = tempSum
        sum = sum +i
    return sum
    
if __name__=="__main__":
    threads = 8
    RangeSum = 100
    taskSum = []
    AmountTask= RangeSum/threads
    pointer= 0
    for thread in range(1,threads+1):
        print(f'thread {thread}')
        data = {
            "start":pointer,
            "end": int(pointer + AmountTask if int(pointer + AmountTask) <= RangeSum else RangeSum)}
        pointer = data["end"]+ 1
        print(data)
        taskSum.append(data)

    start = perf_counter()
    finalSum = 0
    finalSum = sum(range(RangeSum+1))
    end = perf_counter()
    print(f"final using sum from python function {finalSum} in {end - start :0.06f}")

    start = perf_counter()
    finalSum = 0
    finalSum = sumRange(0, RangeSum)
    end = perf_counter()
    print(f"final using UserDefined Sum {finalSum} in {end - start :0.06f}")

    start = perf_counter()
    finalSum = 0
    futures = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        
        for t in taskSum:
            future = executor.submit(sumRange, t['start'], t['end'])
            futures.append(future)
        for i,future in enumerate(futures):
            i = i +1
            print(f"thread {i} result {future.result()} time: {perf_counter()-start :0.06f} ")
            finalSum = finalSum+ future.result()
    end =perf_counter()
    print(
        f"final ThreadPoolExecutor with UserDefined Sum {finalSum} in {end - start :0.06f}")

    start = perf_counter()
    finalSum = 0
    futures = []
    with concurrent.futures.ProcessPoolExecutor() as executor:

        for t in taskSum:
            future = executor.submit(sumRange, t['start'], t['end'])
            futures.append(future)
        for i, future in enumerate(futures):
            i = i + 1
            print(
                f"thread {i} result {future.result()} time: {perf_counter()-start :0.06f} ")
            finalSum = finalSum + future.result()
    end = perf_counter()
    print(f"final ProcessPoolExecutor with UserDefined Sum {finalSum} in {end - start :0.06f}")

    start = perf_counter()
    finalSum = 0
    futures = []
    with concurrent.futures.ProcessPoolExecutor() as executor:

        for t in taskSum:
            future = executor.submit(sum, range(t['start'], t['end']+1))
            futures.append(future)
        for i, future in enumerate(futures):
            i = i + 1
            print(
                f"thread {i} result {future.result()} time: {perf_counter()-start :0.06f} ")
            finalSum = finalSum + future.result()
    end = perf_counter()
    print(f"final ProcessPoolExecutor with Sum function {finalSum} in {end - start :0.06f}")



