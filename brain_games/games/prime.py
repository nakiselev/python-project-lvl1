import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    question = random.randrange(100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def is_prime(num):

    if num <= 1:
        return False
    div = 2
    while num % div != 0:
        div += 1
    return div == num
