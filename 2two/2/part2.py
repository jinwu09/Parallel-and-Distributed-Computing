import time
import concurrent.futures
from pathlib import Path

location = f"{Path.cwd()}/2two/2/testfolder"

def BubbleSort(list):
    for i in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list


def OptBubbleSort(list):
    for i in range(len(list)-1):
        swapped = False

        for j in range(len(list)-1):
            # compare the adjacent elemtns
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True

            # if no number was swapped that means array is sorted now, break the loop
        if (not swapped):
            return list


def InsertionSort(list):
    holePosition = 0
    valueToInsert = 0

    for i in range(len(list)-1):
        # select value to be inserted
        valueToInsert = list[i]
        holePosition = i

        # locate hole positionfor the element to be inserted

        while holePosition > 0 and list[holePosition-1] > valueToInsert:
            list[holePosition] = list[holePosition-1]
            holePosition = holePosition - 1
        # insert the number at hole position
        list[holePosition] = valueToInsert
    return list


def SelectionSort(list):
    for i in range(len(list)):
        # set current elemenet as minimum
        min = i

        # check the elemen to be minimum

        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j

        # swap the minimum element with the current element
        if min != i:
            list[min], list[i] = list[i], list[min]
    return list

def UnmodifiedBubble(fileIndex):
    f = open(f"{location}/data{fileIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()
    start = time.perf_counter()
    sorted = BubbleSort(data)
    # print(sorted)
    time_result = time.perf_counter() - start
    print(
        f"Unmodified bubble sort Set {fileIndex} finished {time_result:0.06f}")
    f = open(f"{location}/Umodified Bubble Sort {fileIndex}.txt", "w")
    f.write(str(data))


def ModifiedBubble(fileIndex):
    f = open(f"{location}/data{fileIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()

    start = time.perf_counter()
    data = OptBubbleSort(data)
    # print(data)
    time_result = time.perf_counter() - start
    print(f"Modified bubble sort Set {fileIndex} finished {time_result:0.06f}")
    f = open(f"{location}/Modified Bubble Sort {fileIndex}.txt", "w")
    f.write(str(data))

def Inserrtion(fileIndex):
    f = open(f"{location}/data{fileIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()

    start = time.perf_counter()
    data = InsertionSort(data)
    # print(data)
    time_result = time.perf_counter() - start
    print(f"Inserrtion sort Set {fileIndex} finished {time_result:0.06f}")
    f = open(f"{location}/InsertionSort {fileIndex}.txt", "w")
    f.write(str(data))

def Selection(fileIndex):
    f = open(f"{location}/data{fileIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()
    start = time.perf_counter()
    data = SelectionSort(data)
    # print(data)
    time_result = time.perf_counter() - start
    print(f"nSelection sort Set {fileIndex} finished {time_result:0.06f}")
    f = open(f"{location}/selection Sort {fileIndex}.txt", "w")
    f.write(str(data))
    
if __name__ =="__main__":
    # do 4 times cause there is 4 files to sort
    length = 4
    print("using ThreadPoolExecutor")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for fileIndex in range(length):
            unmodofiedBubble = executor.submit(UnmodifiedBubble, (fileIndex))
            modifiedBubble = executor.submit(ModifiedBubble, (fileIndex))
            insertionSort = executor.submit(Inserrtion, (fileIndex))
            selectionSort = executor.submit(Selection, (fileIndex))
            futures.append(unmodofiedBubble)
            futures.append(modifiedBubble)
            futures.append(insertionSort)
            futures.append(selectionSort)
    print("using ProcessPoolExecutor")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for fileIndex in range(length):
            unmodofiedBubble = executor.submit(UnmodifiedBubble, (fileIndex))
            modifiedBubble = executor.submit(ModifiedBubble, (fileIndex))
            insertionSort = executor.submit(Inserrtion, (fileIndex))
            selectionSort = executor.submit(Selection, (fileIndex))
            futures.append(unmodofiedBubble)
            futures.append(modifiedBubble)
            futures.append(insertionSort)
            futures.append(selectionSort)

        