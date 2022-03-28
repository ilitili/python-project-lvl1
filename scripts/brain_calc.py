from random import randint

def calc():
    value1 = randint(0,100)
    value2 = randint(0,100)
    print("Question: " + str(value1) + " + " + str(value2))
    calc = value1 + value2
    user_answer = input("Your answer: ")
    if(calc != int(user_answer)):
        print("'" + str(user_answer) + "' is wrong answer ;(. Correct answer was '" + str(calc) + "'")
        return 0
    else:
        print("Correct!")
        return 1
