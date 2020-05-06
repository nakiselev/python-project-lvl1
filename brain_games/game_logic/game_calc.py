import random

OPERATIONS = ['+', '-', '*']


def game_rules():
    print('What is the result of the expression?')


def question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(OPERATIONS)
    que = '{} {} {}'.format(num1, operation, num2)
    ans = eval(que)

    return (que, str(ans))
