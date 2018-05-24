# o(nlog(n))
def find_max_cross_subarray(array, low, mid, high):
    left_sum = array[mid]
    Sum = array[mid]
    left_index = mid
    for i in range(mid-1, low-1, -1):
        Sum += array[i]
        if Sum > left_sum:
            left_sum = Sum
            left_index = i
    right_sum = 0
    Sum = 0
    right_index = mid
    for i in range(mid+1, high+1):
        Sum += array[i]
        if Sum > right_sum:
            right_sum = Sum
            right_index = i
    max_sum = left_sum + right_sum
    return [left_index, right_index, max_sum]


def find_max_subarray(A, low, high):
    if low == high:
        return [low, high, A[low]]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_cross_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        elif cross_sum >= left_sum and cross_sum >= right_sum:
            return [cross_low, cross_high, cross_sum]


# import sys
# n = sys.stdin.readline().strip().split()
# ss = sys.stdin.readline().strip()
# a=([int(i) for i in ss.split()])
# left_index, right_index, subarray_sum = find_max_subarray(a, 0, len(a)-1)
# print(subarray_sum)
