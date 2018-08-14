from random import randint, choice
from eval import calc
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 25)
    y = randint(1, 25)
    op = choice(['+', '-', '*', '/'])
    result = calc(x, y, op)
    z = choice([0, 1, -1])
    disp = result + z
    return[x, y, op, disp]

def check_answer(x, y, op, disp, user_choice):
    if disp == calc(x, y, op):
        if user_choice == True:
            return user_choice
        else:
            return not user_choice
