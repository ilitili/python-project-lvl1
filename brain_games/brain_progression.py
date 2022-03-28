from random import randint

def arithmetic_progression():
    a = randint(1,20)
    b = randint(1,10)
    c = randint(6,10)
    prog_list = []
    for i in range(1,c+1):
        prog_list.append(a+(i-1)*b)
    take_rand = randint(0,c+1)
    rand_num = prog_list[take_rand-2]
    prog_list[take_rand-2] = ".."
    print("Question: ", end= '')
    for i in range(1,prog_list.__len__()):
        print(prog_list[i], end=' ')
    user_answ=input("Your answer: ")
    if(rand_num != int(user_answ)):
        print("'" + str(user_answ) + "' is wrong answer ;(. Correct answer was '" + str(rand_num) + "'")
        return 0
    else:
        print("Correct!")
        return 1
