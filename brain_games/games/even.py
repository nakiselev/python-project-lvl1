import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 20)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (question, correct_answer)
