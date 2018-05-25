# o(log2n)
def Fibonacci_search(array, value, length, low, high):
    n = len(array)
    F_array = Fibonacci_array(length)
    i = 0
    while n > F_array[i] - 1:
        i += 1
    for j in range(n, F_array[i] - 1):   # let the length of array like Fibonacci array
        array.append(array[n - 1])
    while low <= high:
        mid = low + F_array[i - 1] - 1
        if value < array[mid]:
            high = mid - 1
            i -= 1
        elif value > array[mid]:
            low = mid + 1
            i -= 2
        else:
            if mid < n:
                print("out index of value {} in array {}th".format(value, mid + 1))
                return mid
            else:
                print("can't find {} in array".format(value))
                return None


def Fibonacci_array(n):
    '''
    :param n: the length of Fibonacci array
    :return: a Fibonacci array with length of n
    '''
    array = []
    array.append(1)
    array.append(1)
    for i in range(2, n):
        array.append(array[i - 1] + array[i - 2])
    return array


def main():
    a = [-19, -12, 0, 4, 7, 18, 72, 198, 299, 1000]
    Fibonacci_search(a, 7, 20, 0, len(a) - 1)


if __name__ == '__main__':
    main()