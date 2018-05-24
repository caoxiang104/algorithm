import math
def radix_sort(array, d):
    radix = 10
    temp = 1
    for i in range(d):
        array = counting_sort(array, 10, radix, temp)
        temp = temp * radix
    return array


def counting_sort(array, k, radix=10, temp=1):
    c = [0 for _ in range(k)]
    b = [0 for _ in range(len(array))]
    for i in array:
        c[i // temp % radix] = c[i // temp % radix] + 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    for i in array:
        b[c[i // temp % radix - 1]] = i
        c[i // temp % radix - 1] += 1
    return b


def main():
    a = [123, 123, 132, 231, 213, 312, 321]
    a = radix_sort(a, 3)
    print(a)
    print(math.floor(2.3))


if __name__ == '__main__':
    main()