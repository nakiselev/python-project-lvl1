import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def get_question_and_answer():

    start = random.randint(1, 20)
    step = random.randint(1, PROGRESSION_LENGHT)
    hidden_index = random.randint(0, PROGRESSION_LENGHT - 1)

    progression = [str(start + i * step) for i in range(PROGRESSION_LENGHT)]

    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)

    return (question, correct_answer)
