from random import randint
def odd_or_even():
    value = randint(0,100)
    print('Question: ' + str(value))
    if(value%2==0):
        answ = "yes"
    else:
        answ = "no"
    user_answer = input("Your Answer: ")
    if(answ != user_answer):
        print("'" + user_answer + "' is the wrong answer ;(. Correct answer was '" + answ + "'")
        return 0
    else:
        print("Correct!")
        return 1
