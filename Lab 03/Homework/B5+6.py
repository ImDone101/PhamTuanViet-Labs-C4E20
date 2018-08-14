from turtle import *
def draw_star (x, y, length):
    color('blue')
    penup()
    setpos(x, y)
    pendown()
    for i in range (5):
        forward(length)
        right(144)

#test
# draw_star(50,50,50)
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
