
from random import randint

ty = ["Rock","Paper","Scissor"]

bot = ty[randint(0,2)]

user = False

while user ==False:
    user = input("Rock,Paper,Scissor? -->")

    if user == bot:
        print("Tie!")

    elif user == "Rock":
        if bot =="Paper":
            print("You Lose! Computer select -> ", bot)
        else:
            print("You Win! Computer select -> ",bot)

    elif user == "Paper":
        if bot =="Scissor":
            print("You Lose! Computer select -> ", bot)
        else:
            print("You Win! Computer select -> ", bot)

    elif user == "Scissor":
        if bot =="Rock":
            print("You Lose! Computer select -> ", bot)
        else:
            print("You Win! Computer select -> ", bot)

    else:
        print("Invalid Input.Check your spelling!")

    user = False
    bot = ty[randint(0,2)]
