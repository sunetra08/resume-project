import random

num=random.randint(0,30)
number_of_guess=5
value=True
while value:
    n=int(input("GUESS THE NUMBER "))
    if n==num:
        print("CONGRATULATIONS")
        break
    elif n<num:
        print("the number you have entered is lesser than the real number ")
    else:
        print("the number you have entered is greater than the real number ")
    number_of_guess-=1
    print("number of guesses left ",number_of_guess)
    if number_of_guess==0 and n!=num:
        print("you lost ")
        print("the number is ",num)
        break