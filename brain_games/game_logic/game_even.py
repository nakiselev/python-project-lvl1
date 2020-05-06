

import random


def game_rules():
    print('Answer "yes" if number even otherwise answer "no".')


def question_and_answer():
    number = random.randint(1, 20)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (number, correct_answer)
