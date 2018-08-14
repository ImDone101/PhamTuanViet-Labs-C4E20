# def printhl():
#     for i in range(3):
#         print("Hello world")

# printhl()

# def tong(a, b):
#     print(a+b)

# tong(2,3)

from turtle import *
def ve_vuong(dai, mau):
    color(mau)
    for c in range(4):
        forward(dai)
        left(90)

# ve_vuong(100, 'blue')
for i in range(30):
    ve_vuong(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()