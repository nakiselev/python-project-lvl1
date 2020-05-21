import random
from operator import add, sub, mul


OPERATIONS = [('+', add), ('-', sub), ('*', mul)]
DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sign, operation = random.choice(OPERATIONS)
    question = '{} {} {}'.format(num1, sign, num2)
    correct_answer = operation(num1, num2)

    return (question, str(correct_answer))
