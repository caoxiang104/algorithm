from data_structure.Stack.stack import Stack


def num_conversion(stack, num, notation):
    while num:
        stack.push(num % notation)
        num = num // notation
        if stack.size() == stack.limit:
            stack.limit += 1
    return stack


def main():
    num = 12800
    notation = 2
    stack = Stack()
    stack = num_conversion(stack, num, notation)
    # s = ""
    # while not stack.is_empty():
    #     s += str(stack.pop())
    print("{} notation of number {} covert to {} notation is:".format(10, num, notation) +
          "".join(str(stack.pop()) for i in range(stack.size())))


if __name__ == '__main__':
    main()
