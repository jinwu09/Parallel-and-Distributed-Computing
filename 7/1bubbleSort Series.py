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
            break


if __name__ == "__main__":
    # Example usage
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted list:", unsorted_list)

    bubble_sort(unsorted_list)
    print("Sorted list:", unsorted_list)
