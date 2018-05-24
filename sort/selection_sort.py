# o(nlogn)
def selection_sort(array):
    for i in range(0, len(array)-1):
        min_ = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_]:
                min_ = j
        array[i], array[min_] = array[min_], array[i]
    return array


def main():
    a = [1, 3, 2, 4, 6, 5]
    a = selection_sort(a)
    print(a)


if __name__ == '__main__':
    main()