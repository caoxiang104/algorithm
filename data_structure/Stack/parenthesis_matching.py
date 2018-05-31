from data_structure.Stack.stack import Stack


def parenthesis_matching(stack, pare_str):
    stack.limit = len(pare_str)
    for i in pare_str:
        if i == ')' and stack.peek() == '(':
            stack.pop()
        elif i == ']' and stack.peek() == '[':
            stack.pop()
        else:
            stack.push(i)
    return stack.is_empty()


def main():
    stack = Stack()
    examples = ["(([]))", "[]()[()]([])", "[]()[()]([])", "([)"]
    for example in examples:
        print("Balanced parentheses {} is:".format(example) + str(parenthesis_matching(stack, example)))
        while not stack.is_empty(): stack.pop()


if __name__ == '__main__':
    main()