

import random


def game_rules():
    print('Find the greatest common divisor of given numbers.')


def question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    que = '{} {}'.format(num1, num2)

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1

    correct_answer = num1 + num2

    return (que, str(correct_answer))
