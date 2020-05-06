import prompt

LEVELS = 3


def run_game(game_logic):
    print('Welcome to the Brain Games!')
    # game rules
    game_logic.game_rules()

    name = prompt.string('May i have your name: ')
    print('Hello, {}!'.format(name))
    incorrect_text = 'is wrong answer. Correct answer was'

    for level in range(LEVELS):
        que_and_right = game_logic.question_and_answer()
        (question, right) = que_and_right

        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == right:
            print('Correct!')
        else:
            print("'{}' {} '{}'.".format(user_answer, incorrect_text, right))
            print("Let's try again, {}.".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
