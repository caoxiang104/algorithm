# o(n**2)
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


a = [1, 3, 2, 4, 6, 5]
a = bubble_sort(a)
print("a after insertion_sort:", a)