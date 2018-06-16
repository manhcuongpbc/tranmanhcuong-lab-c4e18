from random import randint, choice
# from eval import calc
import eval

x = randint(1,10)
y = randint(1,10)

ops = ['+', '-', '*', '/']
operation = choice(ops)
result = eval.calc(x, y, operation)

# if operation == '+':
#     result = x + y
# elif operation == '-':
#     result = x - y
# elif operation == '*':
#     result = x * y
# elif operation == '/':
#     result = x / y

errs = [-1, 0, 1]
error = choice(errs)

print("{0} {1} {2} = {3}".format(x, operation, y, result + error))

answer = input("y/n ").lower()

if error == 0:
    if answer == 'y':
        print("right")
    else:
        print('wrong')
else:
    if answer == 'y':
        print('wrong')
    else:
        print("right")     