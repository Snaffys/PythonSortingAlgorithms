def merge(arr, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid

    left_array = [0] * left_size
    right_array = [0] * right_size

    for i in range(left_size):
        left_array[i] = arr[left + i]
    for j in range(right_size):
        right_array[j] = arr[mid + 1 + j]

    left_pos = right_pos = 0
    main_pos = left

    while left_pos < left_size and right_pos < right_size:
        if left_array[left_pos] <= right_array[right_pos]:
            arr[main_pos] = left_array[left_pos]
            left_pos += 1
        else:
            arr[main_pos] = right_array[right_pos]
            right_pos += 1
        main_pos += 1

    while left_pos < left_size:
        arr[main_pos] = left_array[left_pos]
        left_pos += 1
        main_pos += 1
    while right_pos < right_size:
        arr[main_pos] = right_array[right_pos]
        right_pos += 1
        main_pos += 1


def _merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        _merge_sort(arr, left, mid)
        _merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge_sort(arr):
    if arr is None:
        return []
    arr = arr.copy()

    _merge_sort(arr, 0, len(arr) - 1)

    return arr

