def heapify(arr, size, ind):
    largest = ind
    left = 2 * ind + 1
    right = 2 * ind + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != ind:
        arr[ind], arr[largest] = arr[largest], arr[ind]
        heapify(arr, size, largest)


def heap_sort(arr):
    if arr is None:
        return []
    arr = arr.copy()
    size = len(arr)

    for ind in range(size // 2 - 1, -1, -1):
        heapify(arr, size, ind)

    for ind in range(size - 1, 0, -1):
        arr[ind], arr[0] = arr[0], arr[ind]
        heapify(arr, ind, 0)

    return arr
