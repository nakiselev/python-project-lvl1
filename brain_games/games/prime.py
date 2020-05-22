import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    question = random.randrange(100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def is_prime(num):

    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
