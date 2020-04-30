
import prompt


def welcome_user(name=''):
    if name == '':
        name = get_username()
    print('Hello, {}!'.format(name))


def ask_question(question):
    return prompt.string(question)


def get_username():
    return ask_question('May I have your name? ')
