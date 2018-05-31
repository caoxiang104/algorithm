class Queue(object):
    class EmptyNode(object):
        '''
        用EmptyNode来实现特殊的空节点
        '''
        pass

    def __init__(self, limit=10):
        super(Queue, self).__init__()
        self.empty = Queue.EmptyNode()
        self.queue = [self.empty for x in range(limit)]
        self.limit = limit
        if limit < 0:
            raise ValueError('limit of queue can not be negative')
        self.head = 0
        self.tail = 0
        self.length = 0

    def __bool__(self):
        return not bool(self.queue)

    def __str__(self):
        super(Queue, self).__str__()
        return str(self.queue)

    def enqueue(self, value):
        '''push an element in the rear of the queue'''
        if self.is_full():
            raise QueueOverflowError
        else:
            self.queue[self.tail] = value
            self.tail += 1
            self.length += 1
        if self.tail >= self.limit:
            self.tail = 0

    def dequeue(self):
        '''pop an element in the front of the queue'''
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            v = self.queue[self.head]
            self.queue[self.head] = self.empty
            self.head += 1
            self.length -= 1
        if self.head >= self.limit:
            self.head = 0
        return v

    def is_full(self):
        return self.head == self.tail and self.queue[self.head] is not self.empty

    def is_empty(self):
        return self.head == self.tail and self.queue[self.head] is self.empty

    def size(self):
        return self.length

    def clear(self):
        while not self.is_empty():
            self.dequeue()

    def rotate(self, index):
        for i in range(index):
            temp = self.queue[self.head]
            self.dequeue()
            self.enqueue(temp)

    def front(self):
        return self.queue[0]


class QueueOverflowError(BaseException):
    pass


def main():
    queue = Queue(12)
    for i in range(10):
        queue.enqueue(i)
    print("Now elements in queue is:" + str(queue))
    queue.dequeue()
    print("After dequeue, elements in queue is:" + str(queue))
    queue.rotate(5)
    print("After rotate one time, elements in queue is:" + str(queue))
    print("Queue is empty?" + str(queue.is_empty()))
    print("Size of queue is:" + str(queue.size()))
    queue.clear()
    print("After clear, queue is empty?" + str(queue.is_empty()))


if __name__ == '__main__':
    main()