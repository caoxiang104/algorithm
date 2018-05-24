# O(n*logn)
def left(i):


























    
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return i//2


def max_heap(array, i, heap_size):
    largest = i
    left_index = left(i)
    right_index = right(i)
    if left_index < heap_size and array[largest] < array[left_index]:
        largest = left_index
    if right_index < heap_size and array[largest] < array[right_index]:
        largest = right_index
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heap(array, largest, heap_size)


def build_max_heap(array, heap_size):
    for i in range(heap_size//2 - 1, -1, -1):
        max_heap(array, i, heap_size)


def heap_sort(array):
    n = len(array)
    build_max_heap(array, n)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        build_max_heap(array, i)
    return array


def main():
    a = [1, 3, 2, 4, 6, 5]
    heap_sort(a)
    print("after heap sort:", a)


if __name__ == '__main__':
    main()


