from random import randint

def gcd():
    value1 = randint(1, 100)
    value2 = randint(1, 100)
    temp1 = value1
    temp2 = value2
    print("Question: " + str(value1) + " " + str(value2))
    answ = input("Your answer: ")
    while(temp1 != temp2):
        if temp1 > temp2:
            temp1 = temp1 - temp2
        else:
            temp2 = temp2 - temp1
    calculated_answer = temp1
    if(calculated_answer != int(answ)):
        print("'" + str(answ) + "' is wrong answer ;(. Correct answer was '" + str(calculated_answer) + "'")
        return 0
    else:
        print("Correct!")
        return 1
