def binary_search(arr, target):
    """
    Returns the index of the target in the sorted array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(arr):
    """
    Sorts the array in place and returns it.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    # Test bubble sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    sorted_arr = bubble_sort(arr.copy())
    print(f"Sorted array: {sorted_arr}")

    # Test binary search
    target = 25
    result_index = binary_search(sorted_arr, target)
    print(f"Index of {target} in sorted array: {result_index}")

if __name__ == "__main__":
    main()