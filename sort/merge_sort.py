# o(nlogn)
def merge_sort(array):
    length = len(array)
    if length > 1:
        half_len = length // 2
        left_arr = merge_sort(array[:half_len])
        right_arr = merge_sort(array[half_len:])
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1
    return array


a = [1, 3, 2, 4, 6, 5]
a = merge_sort(a)
print("a after insertion_sort:", a)