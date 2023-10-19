import multiprocessing


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]


# Divide the list into two parts and sort them in parallel
    with multiprocessing.Pool(2) as pool:
        left = pool.apply_async(merge_sort, (left,))
        right = pool.apply_async(merge_sort, (right,))

        left = left.get()
        right = right.get()

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add the remaining elements from both halves
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Test the merge sort function
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
