def binary_search(array, value, low, high):
    mid = (low + high) // 2
    if value == array[mid]:
        print("out index of value {} in array {}th".format(value, mid + 1))
        return mid
    elif value < array[mid]:
        binary_search(array, value, low, mid - 1)
    else:
        binary_search(array, value, mid + 1, high)


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_search(a, 7, 0, len(a) - 1)


if __name__ == '__main__':
    main()
