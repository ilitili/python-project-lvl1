from cli import *
from brain_even import *
from brain_calc import *
from brain_gcd import *
from brain_progression import *
from brain_prime import *

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i=3
    j=1
    while i!=0 and j != 0:
        j = odd_or_even()
        i-=1
    if j == 0:
        print("Let's try again, " + name + "!")
    else:
        print("Congratulations, " + name + "!")
    print("What is the result of the expression?")
    i = 3
    j = 1
    while i!=0 and j != 0:
        j = calc()
        i-=1
    if j == 0:
        print("Let's try again, " + name + "!")
    else:
        print("Congratulations, " + name + "!")
    print("Find the greatest common divisor of given numbers.")
    i = 3
    j = 1
    while i!=0 and j != 0:
        j = gcd()
        i-=1
    if j == 0:
        print("Let's try again, " + name + "!")
    else:
        print("Congratulations, " + name + "!")
    print("What number is missing in the progression?")
    i = 3
    j = 1
    while i!=0 and j != 0:
        j = arithmetic_progression()
        i-=1
    if j == 0:
        print("Let's try again, " + name + "!")
    else:
        print("Congratulations, " + name + "!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 3
    j = 1
    while i!=0 and j != 0:
        j = prime()
        i-=1
    if j == 0:
        print("Let's try again, " + name + "!")
    else:
        print("Congratulations, " + name + "!")



if __name__ == '__main__':
    main()