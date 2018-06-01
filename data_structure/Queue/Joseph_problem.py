# coding=utf-8
from data_structure.Queue.queue import Queue


def joseph_problem(name_list, k):
    # 约瑟夫问题：每次第k个人死
    queue = Queue(len(name_list))
    for i in name_list:
        queue.enqueue(i)
    while queue.size() != 1:
        queue.rotate(k - 1)
        queue.dequeue()
    return queue.front()


def main():
    name_list = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    result = joseph_problem(name_list, 7)
    print("The surviving people is:" + result)


if __name__ == '__main__':
    main()