import time
import random

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

        while holePosition > 0 and list[holePosition-1]> valueToInsert:
            list[holePosition] = list[holePosition-1]
            holePosition = holePosition -1
        # insert the number at hole position
        list[holePosition]= valueToInsert
    return list

def SelectionSort(list):
    for i in range(len(list)):
        # set current elemenet as minimum
        min = i

        # check the elemen to be minimum

        for j in range(i+1,len(list)):
            if list[j]< list[min]:
                min = j
        
        # swap the minimum element with the current element
        if min != i:
            list[min], list[i] = list[i], list[min]
    return list

length = 4

print("Unmodified bubble sort")
for DataIndex in range(length):
    print(DataIndex)
    f = open(f"data{DataIndex}.txt","r")
    dataStr = f.read()
    data =list(map(int,dataStr.split(", ") ))
    f.close()

    start = time.perf_counter()
    sorted = BubbleSort(data)
    # print(sorted)
    time_result = time.perf_counter() - start
    print(time_result)
    f = open(f"Umodified Bubble Sort {DataIndex}.txt", "w")
    f.write(str(data))


print("\nModified Bublesort")
for DataIndex in range(length):
    print(DataIndex)
    f = open(f"data{DataIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()

    start = time.perf_counter()
    data = OptBubbleSort(data)
    # print(data)
    time_result = time.perf_counter() - start
    print(time_result)
    f = open(f"nModified Bubble Sort {DataIndex}.txt", "w")
    f.write(str(data))

print("\nInsertionSort")
for DataIndex in range(length):
    print(DataIndex)
    f = open(f"data{DataIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()

    start = time.perf_counter()
    data =InsertionSort(data)
    # print(data)
    time_result = time.perf_counter() - start
    print(time_result)
    f = open(f"nInsertionSort {DataIndex}.txt", "w")
    f.write(str(data))

print("\nSelection Sort")
for DataIndex in range(length):
    print(DataIndex)
    f = open(f"data{DataIndex}.txt", "r")
    dataStr = f.read()
    data = list(map(int, dataStr.split(", ")))
    f.close()

    start = time.perf_counter()
    data = SelectionSort(data)
    # print(data)
    time_result = time.perf_counter() - start
    print(time_result)
    f = open(f"election Sort {DataIndex}.txt", "w")
    f.write(str(data))
