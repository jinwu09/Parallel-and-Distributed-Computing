import psutil
import multiprocessing as mp


def counting_sort(arr, exp, process_id, total_processes):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of each digit
    for i in range(process_id, n, total_processes):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count to store the actual position of this digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using count
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output back to arr
    for i in range(process_id, n, total_processes):
        arr[i] = output[i // total_processes]


def radix_sort_parallel(arr):
    max_num = max(arr)
    exp = 1

    total_processes = mp.cpu_count()
    processes = []

    while max_num // exp > 0:
        for i in range(total_processes):
            p = mp.Process(target=counting_sort, args=(
                arr, exp, i, total_processes))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        processes.clear()
        exp *= 10


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

    radix_sort_parallel(IntData)
    print("Radix sort")
    print_memory_usage()
