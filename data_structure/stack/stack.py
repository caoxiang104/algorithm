# coding=utf-8
class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return not bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        '''push a data to the top of the stack'''
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        else:
            self.stack.append(data)

    def pop(self):
        '''pop a data from the top of the stack'''
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop a data from an empty stack")

    def peek(self):
        '''Peek at the top-most element of the stack'''
        return self.stack[-1]

    def is_empty(self):
        '''judge a stack whether an empty stack or not'''
        return not bool(self.stack)

    def clear(self):
        '''clear a stack'''
        while len(self.stack):
            self.stack.pop()

    def size(self):
        '''size of stack'''
        return len(self.stack)


class StackOverflowError(BaseException):
    pass


def main():
    stack = Stack()
    stack.limit = 20
    print("Initial stack:" + str(stack))
    for i in range(20):
        stack.push(i)
    print("Stack after push operator:" + str(stack))
    stack.pop()
    print("Stack after pop operator:" + str(stack))
    stack.pop()
    print("The last data in stack is:" + str(stack.peek()))
    print("The size of stack is:" + str(stack.size()))
    print("The stack is empty?" + str(stack.is_empty()))
    print("The stack is empty?" + str(stack.clear()))


if __name__ == '__main__':
    main()