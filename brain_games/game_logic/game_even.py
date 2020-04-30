import brain_games.cli as cli
import random


def game():
    true_answer = 0
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = cli.get_username()
    while true_answer < 3:
        number = random.randint(1, 20)
        print('Question:', number)
        answer = cli.ask_question('Your answer: ')

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer.lower() == correct_answer:
            true_answer += 1
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}".format(name))
            return
    print('Congratulations')
