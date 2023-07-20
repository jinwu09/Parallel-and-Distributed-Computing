from time import perf_counter
import numpy as np
import concurrent.futures

def enumeration_sortCPython(arr):
    # Create an enumerated list from the input array
    enumerated_list = list(enumerate(arr))

    # Sort the enumerated list based on the values
    sorted_list = sorted(enumerated_list, key=lambda x: x[1])

    # Extract the original array elements from the sorted enumerated list
    sorted_arr = [element for index, element in sorted_list]

    return sorted_arr


def enumeration_sort(arr):
    enumerated_list = list(enumerate(arr))

    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if enumerated_list[j][1] < enumerated_list[min_index][1]:
                min_index = j

        enumerated_list[i], enumerated_list[min_index] = enumerated_list[min_index], enumerated_list[i]

    sorted_arr = [element for index, element in enumerated_list]
    return sorted_arr


def parallel_enumeration_sort(arr,threads):
    chunk_size = len(arr) // threads
    chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        sorted_chunks = executor.map(enumeration_sort, chunks)

    sorted_arr = []
    for chunk in sorted_chunks:
        sorted_arr.extend(chunk)

    return sorted_arr

if __name__=="__main__":
    data = ""
    maxRange = 500
    with open(f"./miniResearch/data/data{maxRange}.txt", 'r') as f:
        data = f.read()
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(', ')
    IntData = []
    for i in data:
        IntData.append(int(i))


    startTime = perf_counter()
    sortedData = enumeration_sort(IntData)
    endTime = perf_counter()
    print(f"serial this takes about {endTime - startTime:0.6f}")
    with open(f"./miniResearch/data/result{maxRange}.txt", "w") as f:
        f.write(str(sortedData))

    threads = 4
    tasks = np.array_split(IntData,threads)
    arr = IntData

    startTime = perf_counter()
    results = parallel_enumeration_sort(IntData,threads)    
    endTime = perf_counter()
    with open(f"./miniResearch/data/ProcessResult{maxRange}.txt", "w") as f:
        f.write(str(sortedData))

    print(f"process takes about {endTime - startTime:0.6f}")