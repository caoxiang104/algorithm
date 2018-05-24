import random


def randomized_select(array, p, r, i):
    '''
    :param array: input array
    :param p: start index
    :param r: end index
    :param i: value of ith min value
    :return: array
    '''
    if p == r:
        return array[p]
    q = randomized_partition(array, p, r)
    k = q - p + 1
    if i == k:
        return array[q]
    elif i < k:
        return randomized_select(array, p, q - 1, i)
    else:
        return randomized_select(array, q + 1, r, i - k)


def randomized_partition(array, p, r):
    '''
    :param array: input array
    :param p: start index
    :param r: end index
    :return: the result of sort
    '''
    q = random.randint(p, r)
    array[r], array[q] = array[q], array[r]
    x = array[r]
    j = p - 1
    for i in range(p, r):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[j + 1], array[r] = array[r], array[j + 1]
    return j + 1


def main():
    a = [1, 3, 4, 5, 6, 2]
    i = 5
    out = randomized_select(a, 0, len(a) - 1, i)
    print("array of a:", a, "{}th min value:".format(i), out)


if __name__ == '__main__':
    main()