from turtle import *
def draw_square(length, col):
    color(col)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()

draw_square(50, 'red')