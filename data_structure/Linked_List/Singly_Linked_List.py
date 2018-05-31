# coding=utf-8
# 实现带哨兵的单链表


class LinkedList(object):
    class Node(object):
        def __init__(self, value, next_node):
            super(LinkedList.Node, self).__init__()
            self.value = value
            self.next = next_node

        def __str__(self):
            super(LinkedList.Node, self).__str__()
            return str(self.value)

    def __init__(self, *arg):
        super(LinkedList, self).__init__()
        self.nil = LinkedList.Node(None, None)
        self.nil.next = self.nil
        self.length = 0
        for value in arg:
            self.append(value)

    def append(self, value):
        temp_node = self.nil
        node = LinkedList.Node(value, temp_node)
        while temp_node.next is not self.nil:
            temp_node = temp_node.next
        temp_node.next = node
        self.length += 1
        return self.length

    def prepend(self, value):
        temp_node = self.nil
        node = LinkedList.Node(value, temp_node.next)
        temp_node.next = node
        self.length += 1
        return self.length

    def insert(self, index, value):
        cur_node = self.nil
        cur_pos = 0
        if index > self.size():
            raise IndexError("Can't insert value beyond the list")
        while cur_pos < index:
            cur_node = cur_node.next
            cur_pos += 1
        node = LinkedList.Node(value, cur_node.next)
        cur_node.next = node
        self.length += 1
        return self.length

    def delete(self, value):
        cur_node = self.nil.next
        temp_node = self.nil
        while cur_node is not self.nil:
            if cur_node.value == value:
                break
            else:
                cur_node = cur_node.next
                temp_node = temp_node.next
        if cur_node is not self.nil:
            temp_node.next = cur_node.next
            self.length -= 1
        return cur_node.value

    def search(self, value):
        cur_node = self.nil.next
        while cur_node is not self.nil and cur_node.value != value:
            cur_node = cur_node.next
        return cur_node.value

    def size(self):
        return self.length

    def __str__(self):
        super(LinkedList, self).__str__()
        cur_node = self.nil.next
        link_ = []
        while cur_node is not self.nil:
            link_.append(str(cur_node))
            cur_node = cur_node.next
        return '[' + ",".join(link_) + ']'


def main():
    link_ = LinkedList(2, 3, 5)
    print(link_)
    for i in range(10):
        link_.append(i)
    print(link_)
    link_ = LinkedList(1, 2, 3)
    for i in range(10):
        link_.prepend(i)
    print(link_)
    print(link_.size())
    link_.insert(2, 100)
    print(link_)
    link_.delete(2)
    print(link_)
    print(link_.search(100))


if __name__ == '__main__':
    main()