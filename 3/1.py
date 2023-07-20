from time import perf_counter
import concurrent.futures

def printNames(thread:int):
    print(f"Thread: {thread}")

def ThreadFunction(threads):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for thread in range(1,threads+1):
            task = executor.submit(printNames,thread)


if __name__=="__main__":
    threads = int(input())
    startTime = perf_counter()
    endTime = perf_counter()
    ThreadFunction(threads)
    print(f"it took about : {endTime-startTime}")
