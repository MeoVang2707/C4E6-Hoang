from random import *
def generate_quiz():
    num1 = randint(1,15)
    num2 = randint(1,10)
    sign = choice(['+','-','*','/'])
    if sign == '+':
        answer = num1 + num2 + choice([-1,0,1])
    elif sign == '-':
        answer = num1 - num2 + choice([-1,0,1])
    elif sign == '*':
        answer = num1 * num2 + choice([-1,0,1])
    else:
        answer = num1/num2 + choice([-1,0,1])
    return [num1, num2, sign, answer]
    
def check_answer(num1, num2, sign, answer, user_choice):
    if sign == '+':
        answer_true = num1 + num2
    elif sign == '-':
        answer_true = num1 - num2
    elif sign == '*':
        answer_true = num1 * num2
    else:
        answer_true = num1/num2
    if answer==answer_true:
        if user_choice==True:
            return True
        else:
            return False
    else:
        if user_choice==False: 
            return True
        else:
            return False

