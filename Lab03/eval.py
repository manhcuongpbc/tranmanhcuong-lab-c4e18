from random import choice


def calc(x, y, operation):

    # operation = choice(['+', '-', '*', '/'])

    result = 0

    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        result = x / y
    # print(result)
    return result

# print("hello world")
# res = calc(4, 7, '*')
# print(res)