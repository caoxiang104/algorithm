# coding=utf-8
from data_structure.Stack.stack import Stack


def infix_to_suffix(list_):
    stack_suffix = Stack(20)
    stack_character = Stack(20)
    for i in list_:
        if i.isalnum():
            stack_suffix.push(i)
        elif i == '(':
            stack_character.push(i)
        elif i in ['+', '-']:
            while not stack_character.is_empty() and stack_character.peek() != '(':
                stack_suffix.push(stack_character.peek())
                stack_character.pop()
            stack_character.push(i)
        elif i in ['*', '/']:
            while not stack_character.is_empty() and stack_character.peek() in ['*', '/']:
                stack_suffix.push(stack_character.peek())
                stack_character.pop()
            stack_character.push(i)
        elif i == ')':
            while not stack_character.is_empty() and stack_character.peek() != '(':
                stack_suffix.push(stack_character.peek())
                stack_character.pop()
            stack_character.pop()
    while not stack_character.is_empty():
        stack_suffix.push(stack_character.peek())
        stack_character.pop()
    return stack_suffix


def process_string(string):
    '''处理字符串'''
    temp = ""
    b = []
    for i in range(len(string)):
        if string[i].isalnum():
            temp += string[i]
            continue
        else:
            if len(temp) != 0:
                b.append(temp)
                temp = ""
            b.append(string[i])
    if string[len(string) - 1].isalnum():
        b.append(temp)
    return b


def cal_formula(stack_):
    list_ = []
    while not stack_.is_empty():
        list_.append(stack_.peek())
        stack_.pop()
    list_.reverse()
    stack = Stack(20)
    for i in list_:
        if i.isalnum():
            stack.push(int(i))
        elif i in ['+', '-', '*', '/']:
            temp2 = stack.peek()
            stack.pop()
            temp1 = stack.peek()
            stack.pop()
            if i == '+':
                temp = temp1 + temp2
            elif i == '-':
                temp = temp1 - temp2
            elif i == '*':
                temp = temp1 * temp2
            elif i == '/':
                temp = temp1 / temp2
            stack.push(temp)
    out = stack.peek()
    stack.pop()
    return out


def main():
    a = "(31+42*53)*(6+7)"
    b = process_string(a)
    print("after process string:", b)
    c = infix_to_suffix(b)
    print("infix turn to suffix is:", c)
    print("The result of calculating the formula is:",cal_formula(c))


if __name__ == '__main__':
    main()
