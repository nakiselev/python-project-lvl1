

import random


def game_rules():
    print('What number is missing in the progression?')


def question_and_answer():

    step = random.randint(1, 10)
    start = random.randint(1, 20)
    hide = random.randint(1, 10)

    que = ''

    for number in range(10):
        if number == hide:
            correct_answer = start
            que += '.. '
        else:
            que += str(start) + ' '

        start += step

    return (que, str(correct_answer))