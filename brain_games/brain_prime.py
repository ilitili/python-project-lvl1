from random import randint

def prime():
    num = randint(1,100)
    if num>1:
        for i in range(2, int(num/2)+1):
            if(num%i)==0:
                answ = "no"
                break
        else:
            answ = "yes"
    else:
        answ = "no"
    print('Question: ' + str(num))
    user_answ = input("Your answer: ")
    if answ != str(user_answ):
        print("'" + str(user_answ) + "' is wrong answer ;(. Correct answer was '" + str(answ) + "'")
        return 0
    else:
        print("Correct!")
        return 1