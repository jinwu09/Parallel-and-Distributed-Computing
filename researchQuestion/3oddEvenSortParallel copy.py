import psutil
import concurrent.futures


def parallel_oddeven_sort(arr):
    def oddeven_sort_phase(arr, is_odd):
        start = 1 if is_odd else 0
        for i in range(start, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    n = len(arr)
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        for i in range(n):
            if i % 2 == 0:
                executor.submit(oddeven_sort_phase, arr, True)
            else:
                executor.submit(oddeven_sort_phase, arr, False)


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

    parallel_oddeven_sort(IntData)
    print("parallel_odd_even_sort")
    print_memory_usage()
