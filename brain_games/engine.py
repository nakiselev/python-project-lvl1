import prompt

MAX_LEVEL = 3


def play(game_logic):
    print('Welcome to the Brain Games!')
    # game description
    print(game_logic.DESCRIPTION)
    # ask player name
    name = prompt.string('May i have your name: ')
    print('Hello, {}!'.format(name))
    incorrect_text = 'is wrong answer. Correct answer was'

    for level in range(MAX_LEVEL):
        question, correct_answer = game_logic.get_question_and_answer()

        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' {} '{}'.".format(user_answer,
                                         incorrect_text,
                                         correct_answer))
            print("Let's try again, {}.".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
