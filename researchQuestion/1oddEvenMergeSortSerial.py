import psutil
import multiprocessing as mp


def odd_even_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(arr1, arr2):
        merged = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged

    def odd_even_merge(arr):
        if len(arr) <= 1:
            return arr

        odd = odd_even_merge(arr[1::2])
        even = odd_even_merge(arr[::2])
        return merge(odd, even)

    sorted_arr = odd_even_merge(arr)
    return sorted_arr


def merge(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


def print_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    print(f"Memory Usage: {mem_info.rss} bytes")


if __name__ == "__main__":
    print("start state array:")
    print_memory_usage()

    data = ""
    with open(f"./miniResearch/data/data1000000.txt", 'r') as f:
        data = f.read()
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(', ')
    IntData = []
    for i in data:
        IntData.append(int(i))

    # Example usage:
    print("Original array:")
    print_memory_usage()

    sorteddata = odd_even_merge_sort(IntData)
    print("odd even merge sort")
    print_memory_usage()
