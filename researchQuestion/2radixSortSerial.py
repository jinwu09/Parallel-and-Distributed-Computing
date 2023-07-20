import psutil


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
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

    radix_sort(IntData)
    print("Radix sort")
    print_memory_usage()
