import multiprocessing


def parallel_bubble_sort(arr):
    n = len(arr)
    with multiprocessing.Manager() as manager:
        shared_list = manager.list(arr)
        with multiprocessing.Pool() as pool:
            for i in range(n):
                # Flag to check if any swaps occurred in this pass
                swapped = manager.Value('i', 0)

                # Perform the bubble sort in parallel
                results = pool.starmap_async(
                    compare_and_swap, [(shared_list, swapped, j) for j in range(1, n - i)])
                results.wait()

                # Check if any swaps occurred and break the loop if no swaps occurred
                if swapped.value == 0:
                    break

            arr[:] = shared_list[:]


def compare_and_swap(arr, swapped, j):
    if arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        swapped.value = 1


if __name__ == "__main__":
    # Example usage
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted list:", unsorted_list)

    parallel_bubble_sort(unsorted_list)
    print("Sorted list:", unsorted_list)
