import psutil
import os


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


def block_sort(arr, block_size):
    n = len(arr)

    def block_merge_sort(block):
        if len(block) <= 1:
            return block

        odd = block_merge_sort(block[1::2])
        even = block_merge_sort(block[::2])
        return merge(odd, even)

    # Divide the input array into blocks
    blocks = [arr[i:i + block_size] for i in range(0, n, block_size)]

    # Sort each block serially
    blocks = [block_merge_sort(block) for block in blocks]

    # Merge the sorted blocks using odd-even merging
    while len(blocks) > 1:
        next_blocks = []
        for i in range(0, len(blocks) - 1, 2):
            merged = merge(blocks[i], blocks[i + 1])
            next_blocks.append(merged)

        if len(blocks) % 2 != 0:
            next_blocks.append(blocks[-1])

        blocks = next_blocks

    sorted_arr = blocks[0]
    return sorted_arr


def print_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    print(f"Memory Usage: {mem_info.rss} bytes")


if __name__ == "__main__":
    print("start state array:")
    print_memory_usage()
    print(os.getcwd())
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
    block_size = 5
    IntData = block_sort(IntData, block_size)
    print("block_sort")
    print_memory_usage()
