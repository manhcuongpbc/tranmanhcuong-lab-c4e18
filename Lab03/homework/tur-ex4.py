from turtle import *
def draw_square(length, col):
    color(col)
    for j in range(4):
        forward(length)
        left(90)
    # mainloop()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
