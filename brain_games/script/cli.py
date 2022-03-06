import prompt

def welcome_user():
    print('brain-games')
    print('Welcome to Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name




