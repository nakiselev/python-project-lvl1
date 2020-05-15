import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1

    return num1 + num2


def get_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    question = '{} {}'.format(num1, num2)
    correct_answer = get_gcd(num1, num2)

    return (question, str(correct_answer))
