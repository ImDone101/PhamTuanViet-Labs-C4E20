x = int(input("x = "))
chon = input("Operation (+, -, *, /): ")
y = int(input("y = "))
if chon == '+':
    kq = x + y
elif chon == '-':
    kq = x - y
elif chon == '*':
    kq = x * y
elif chon == '/':
    kq = x / y
else:
    print("Khong co")


print("{} {} {} = ".format(x, chon, y), kq)

