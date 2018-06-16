from turtle import *

def draw_star(x, y, length):
    up()
    ht()
    goto(x, y)
    for i in range(5):
        forward(length)
        left(144)
    # mainloop()

speed(-1)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
