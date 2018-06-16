from random import *
import eval

def generate_quiz():
    #Hint: Return [x, y, op, result]

    x = randint(1,10)
    y = randint(1,10)

    ops = ['+', '-', '*', '/']
    op = choice(ops)
    result = eval.calc(x, y, op)
    errs = [-1, 0, 1]
    error = choice(errs)

    return [x, y, op, result + error]

def check_answer(x, y, op, display_result, user_choice):
    print(user_choice)
    # x, y, op, result = generate_quiz()
    result = eval.calc(x, y, op)
    if result == display_result and user_choice == True\
        or result  != display_result and user_choice == False:
        mark = True
    else:
        mark = False
    return mark


