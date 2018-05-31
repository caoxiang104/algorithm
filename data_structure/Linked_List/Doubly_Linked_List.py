# coding=utf-8
"""
实现带哨兵的双向循环链表
"""


class LinkedList(object):
    class Node(object):
        def __init__(self, value, prev_node, next_node):
            super(LinkedList.Node, self).__init__()
            self.value = value
            self.prev = prev_node
            self.next = next_node

        def __str__(self):
            super(LinkedList.Node, self).__str__()
            return str(self.value)

    def __init__(self, *arg):
        super(LinkedList, self).__init__()
        self.nil = LinkedList.Node(None, None, None)
        self.nil.prev = self.nil
        self.nil.next = self.nil
        self.length = 0
        for value in arg:
            self.append(value)

    def append(self, value):
        # 在链表末端加入元素
        temp_node = self.nil.prev
        node = LinkedList.Node(value, temp_node, self.nil)
        temp_node.next = node
        self.nil.prev = node
        self.length += 1
        return self.length

    def prepend(self, value):
        # 在链表前端加入元素
        temp_node = self.nil.next
        node = LinkedList.Node(value, self.nil, temp_node)
        self.nil.next = node
        temp_node.prev = node
        self.length += 1
        return self.length

    def size(self):
        return self.length

    def __str__(self):
        super(LinkedList, self).__str__()
        cur_node = self.nil.next
        list_ = []
        while cur_node is not self.nil:
            list_.append(str(cur_node))
            cur_node = cur_node.next
        # print(list_)
        return '[' + ",".join(list_) + ']'

    def delete(self, value):
        # 删除元素
        cur_node = self.nil.next
        while cur_node is not self.nil:
            if cur_node.value == value:
                break
            else:
                cur_node = cur_node.next
        if cur_node is not self.nil:
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
            self.length -= 1
        return cur_node.value

    def search(self, value):
        # 查找一个元素是否在链表中
        cur_node = self.nil.next
        while cur_node is not self.nil and cur_node.value != value:
            cur_node = cur_node.next
        return cur_node.value

    def insert(self, index, value):
        # 在index后的位置插入value
        if index > self.size():
            raise IndexError("Can't insert value beyond the list")
        cur_pos = 0
        cur_node = self.nil
        while cur_pos < index:
            cur_node = cur_node.next
            cur_pos += 1
        node = LinkedList.Node(value, cur_node, cur_node.next)
        cur_node.next.prev = node
        cur_node.next = node
        self.length += 1
        return self.length


def main():
    link_ = LinkedList(100, 200)
    for i in range(9):
        link_.append(i)
    print(link_)
    link_ = LinkedList(100, 200)
    for i in range(9):
        link_.prepend(i)
    print(link_)
    link_.delete(100)
    print(link_)
    link_.insert(2,99)
    print(link_)
    print(link_.search(99))


if __name__ == '__main__':
    main()
