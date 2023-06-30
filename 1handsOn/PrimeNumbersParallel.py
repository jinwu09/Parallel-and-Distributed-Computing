from time import perf_counter
import concurrent.futures 
import numpy as np

threads = 2
maxNumber = 25000

def Prime(task):
    primeNum = []
    for num in task:
        if num == 1:
            # print(num, "is not a prime number")
            None
        elif num > 1:
           # check for factors
           for i in range(2, num):
                if (num % i) == 0:
                #    print(num, "is not a prime number")
                #    print(i, "times", num//i, "is", num)
                    break
                else:
                    # print(num,"is a prime number")
                    primeNum.append(num)
                    break
        else:
            #    print(num, "is not a prime number")
            None
    return primeNum

if __name__=="__main__":
    allPrime = []
    startTime = perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        taskArray = (np.array_split(range(1,maxNumber+1),threads))
        # print(taskArray)
        for task in taskArray:
            future = executor.submit(Prime,task)
            futures.append(future)

        for future in futures:
            allPrime+=future.result()
    endTime = perf_counter()
    # print(allPrime)
    print(f"Parallel takes about: {endTime-startTime:0.06f}")

    allPrime = []
    startTime = perf_counter()
    Sequential =Prime(range(1,maxNumber+1))
    endTime = perf_counter()
    # print(Sequential)
    print(f"Sequential takes about: {endTime-startTime:0.06f}")



        

    

