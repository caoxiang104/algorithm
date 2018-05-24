def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return i // 2


def max_heap(array, index, heap_size):
    largest = index
    left_index = left(index)
    right_index = right(index)
    if left_index < heap_size and array[largest] < array[left_index]:
        largest = left_index
    if right_index < heap_size and array[largest] < array[right_index]:
        largest = right_index
    if index != largest:
        array[index], array[largest] = array[largest], array[index]
        max_heap(array, largest, heap_size)


def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1,  -1, -1):
        max_heap(array, i, n)
    return array


def heap_maximum(array):
    return array[0]


def heap_extract_max(array):
    len_ = len(array)
    array[0], array[len_ - 1] = array[len_ - 1], array[0]
    max_ = array[len(array) - 1]
    array.pop(len_ - 1)
    max_heap(array, 0, len_ - 1)
    return max_


def heap_increase_key(array, index, key):
    if array[index] > key:
        print("new key is small than current key")
        return
    array[index] = key
    parent_index = parent(index)
    while index > 0 and array[parent_index] < array[index]:
        array[parent_index], array[index] = array[index], array[parent_index]
        index = parent_index
        parent_index = parent(index)


def heap_insert(array, key):
    array.append(float('-Inf'))
    print("array:", array)
    heap_increase_key(array, len(array) - 1, key)


def main():
    a = [1, 6, 3, 2, 4, 5]
    a = build_max_heap(a)
    print("max heap:", a)
    max_2 = heap_maximum(a)
    print("max heap key:", max_2)
    max_1 = heap_extract_max(a)
    print("max heap key:", max_1)
    print("array after extract max:", a)
    heap_increase_key(a, 2, 9)
    print("increase index in 2 to the key value of 9:", a)
    heap_insert(a, 8)
    print("insert value of 8 in heap", a)


if __name__ == '__main__':
    main()
