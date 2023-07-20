from time import perf_counter
import concurrent.futures
import math


if __name__=="__main__":
    numbers = [4,5,6,7]
    startTime = perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for number in numbers:
            task = executor.submit(math.factorial,number)
            futures.append(task)
        for i, future in enumerate(futures):
            print(f"thread:{i} factorial of : {future.result()}")
            print("hi")
    endTime = perf_counter()
    print(f"it took about : {endTime-startTime}")
