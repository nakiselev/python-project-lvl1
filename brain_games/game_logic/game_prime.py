import random


def game_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question_and_answer():

    num = random.randrange(100)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return (num, correct_answer)


def is_prime(num):
    div = 2
    while num % div != 0:
        div += 1
    return div == num