# O(log2n)
def insertion_search(array, value, low, high):
    mid = int(low + (value - array[low]) / (array[high] - array[low]) * (high - low))
    if value == array[mid]:
        print("out index of value {} in array {}th".format(value, mid + 1))
        return mid
    elif value < array[mid]:
        return insertion_search(array, value, low, mid - 1)
    else:
        return insertion_search(array, value, mid + 1, high)


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    insertion_search(a, 7, 0, len(a) - 1)


if __name__ == '__main__':
    main()