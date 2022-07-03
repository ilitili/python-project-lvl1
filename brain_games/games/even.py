"""Even game engine."""

import random

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_challenge():
    """Return question and answer for the game 'even'.
    Returns:
        question(str): random number in range from 1 to 100
        answer(str): 'yes' - number is prime, 'no' - number is not prime.
    """
    random_number = random.randint(1, 100)
    question = str(random_number)
    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
