import random
guess = ["snake", "water", "gun"]
count = 0
while True:
    m = random.choice(guess)
    user = input("enter between snake / water / gun : ")
    print("computer-s choice ", m)
    if m == "snake" and user == "gun":
        print("gun kill the snake and gun win")
        count += 1
        print("your score is ", count)
    elif m == "gun" and user == "water":
        print("gun drown in the water and water win")
        count += 1
        print("your score is ", count)
    elif m == "water" and user == "snake":
        print("snake drinks the water and snake wins")
        count += 1
        print("your score is ", count)
    elif m == user:
        print("its a tie")
    else:
        print("you lost ")
    turn = input("do you want to continue with the game (y/n) : ")
    if turn == "n":
        print("thank you for playing with us \n your final score is ", count)
        break
    elif turn != "n" and turn != "y":
        print("Your choice is not correct")
