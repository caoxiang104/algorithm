# o(nlogn)
def partition(array, p, r):
    i = p - 1
    x = array[r]
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


def main():
    a = [1, 3, 2, 4, 6, 5]
    quick_sort(a, 0, len(a) - 1)
    print("a after quick_sort:", a)


if __name__ == '__main__':
    main()