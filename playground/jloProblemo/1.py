# make a program that sums all even numbers with thread pool executor
import numpy as np
import concurrent.futures


if __name__ == "__main__":
    maxRange = 100
    thread = 5
    array = []
    for num in range(1,maxRange +1):
        if num % 2 == 0 :
            array.append(num)

    taskArray =(np.array_split(array,thread))
    finalSum = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(sum,taskArray)
        for result in results:
            finalSum += result
    print(f"this is the sum: {finalSum}")