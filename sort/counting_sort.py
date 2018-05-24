# O(n)
def counting_sort(array, k):
    c = []
    b = []
    for i in range(0, k + 1):
        c.append(0)
    for i in range(len(array)):
        b.append(0)
        c[array[i]] += 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    print("length of array b:", len(b), "length of array a:", len(array), "length of array c:", len(c))
    for i in range(len(array)):
        b[c[array[i]] - 1] = array[i]
        c[array[i]] -= 1
    return b


def main():
    a = [2, 5, 3, 0, 2, 3, 0, 3]
    out = counting_sort(a, 5)
    print("array after counting sort:", out)


if __name__ == '__main__':
    main()
