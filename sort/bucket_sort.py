import math


def bucket_sort(array):
    n = len(array)
    b = [list() for _ in array]
    for i in array:
        index = math.floor(n * i)
        b[int(index)].append(i)
    for i in range(n):
        insert_sort(b[i])
    out = []
    for i in b:
        for j in i:
            out.append(j)
    return out


def insert_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def main():
    a = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    a = bucket_sort(a)
    print("after bucket sort:", a)


if __name__ == '__main__':
    main()