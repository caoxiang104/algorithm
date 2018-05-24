# o(nlogn)
import random


def random_quick_sort(array, p, r):
    if p < r:
        q = random_partition_sort(array, p, r)
        random_quick_sort(array, p, q - 1)
        random_quick_sort(array, q + 1, r)


def random_partition_sort(array, p, r):
    i = random.randint(p, r)
    array[r], array[i] = array[i], array[r]
    return partition(array, p, r)


def partition(array, p, r):
    i = p - 1
    x = array[r]
    for j in range(p, r):
        if array[j] < x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def main():
    a = [1, 3, 2, 4, 6, 5]
    random_quick_sort(a, 0, len(a)-1)
    print("after random quick sort:", a)


if __name__ == '__main__':
    main()