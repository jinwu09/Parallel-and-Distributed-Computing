def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def mergeBubbleSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = bubble_sort(left_half)
    right_half = bubble_sort(right_half)

    return merge(left_half, right_half)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps occurred in this pass
        swapped = False

        # Perform the bubble sort
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True

        # If no swaps occurred in this pass, the list is already sorted
        if not swapped:
            return arr
            break


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
    sorted_arr = mergeBubbleSort(arr)
    print("Sorted array:", sorted_arr)
