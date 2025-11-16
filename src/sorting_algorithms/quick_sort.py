def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        _quick_sort(arr, low, p - 1)
        _quick_sort(arr, p + 1, high)


def quick_sort(arr):
    if arr is None:
        return []
    arr = arr.copy()

    _quick_sort(arr, 0, len(arr) - 1)

    return arr

