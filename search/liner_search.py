# o(n)
def liner_search(array, value):
    temp = -1
    for index, i in enumerate(array):
        if value == i:
            temp = 1
            print("out index of value {} in array {}th".format(value, index + 1))
    if temp == -1:
        print("can't find {} in array".format(value))


def main():
    a = [1, 2, 3, 4, 5, 6]
    value = 7
    liner_search(a, value)


if __name__ == '__main__':
    main()