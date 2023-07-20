import psutil
import multiprocessing as mp


def odd_even_sort(arr):
    n = len(arr)
    sorted = False

    while not sorted:
        sorted = True
        # Perform odd-even sort on odd indices
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        # Perform odd-even sort on even indices
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False


def parallel_odd_even_sort(arr):
    n = len(arr)
    processes = []

    while True:
        sorted = True

        # Perform odd-even sort on odd indices in parallel
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                sorted = False
                p = mp.Process(target=swap_elements, args=(arr, i, i + 1))
                processes.append(p)
                p.start()

        # Wait for processes to finish
        for p in processes:
            p.join()

        processes.clear()

        # Perform odd-even sort on even indices in parallel
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                sorted = False
                p = mp.Process(target=swap_elements, args=(arr, i, i + 1))
                processes.append(p)
                p.start()

        # Wait for processes to finish
        for p in processes:
            p.join()

        processes.clear()

        if sorted:
            break


def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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

    parallel_odd_even_sort(IntData)
    print("parallel_odd_even_sort")
    print_memory_usage()
