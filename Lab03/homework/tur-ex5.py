from turtle import *


def draw_star(x, y, length):
    up()
    ht()
    goto(x, y)
    for i in range(5):
        forward(length)
        left(144)
    mainloop()

draw_star(10, 10, 50)