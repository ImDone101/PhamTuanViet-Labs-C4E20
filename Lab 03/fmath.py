from random import randint, choice
# from eval import calc
import eval
x = randint(1, 25)
y = randint(1, 25)
phep = ['+', '-', '*', '/']
use = choice(phep)
err = ['0', '-1', '1']
z = int(choice(err))

kq = eval.calc(x, y, use)

disp = kq + z
print("{} {} {} = {}".format(x, use, y, disp))
choose = input("Y or N: ").upper()
if choose == 'Y':
    if z == 0:
        print("Dung")
    else:
        print("Sai")
elif choose == 'N':
    if z == 0:
        print("Sai")
    else:
        print("Dung")
pass
