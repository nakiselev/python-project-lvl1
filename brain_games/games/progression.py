import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def get_question_and_answer():

    start = random.randint(1, 20)
    step = random.randint(1, PROGRESSION_LENGHT)
    hidden_index = random.randint(0, PROGRESSION_LENGHT - 1)
    question = ''

    for i in range(PROGRESSION_LENGHT):

        number = start + i * step
        if i == hidden_index:
            correct_answer = number
            question += '.. '
        else:
            question += str(number) + ' '

    return (question, str(correct_answer))
