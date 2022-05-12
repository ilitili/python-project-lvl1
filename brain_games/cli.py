import prompt


def welcome_user():  # function name from step 3 of project
    """Welcome dialog."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


