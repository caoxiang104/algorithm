# O(n**2)
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


a = [1, 3, 2, 4, 6, 5]
a = insertion_sort(a)
print("a after insertion_sort", a)