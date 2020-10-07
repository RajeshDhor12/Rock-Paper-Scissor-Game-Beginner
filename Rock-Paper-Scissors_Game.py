# The original code can be found in OriginalCode.py and the last version I updated is in PreviousCode.py
import random

print("Rock-Paper-Scissor Game\n 1.Rock \n 2.Paper \n 3.Scissor\n 4.To Stop the Game")


def main(inputU, inputB):
    options = ["Rock", "Paper", "Scissor"]
    if inputU == inputB:
        print("Tie, both players played " + options[inputU - 1])
    elif inputU + inputB == 3:
        if inputU > inputB:
            print("You win, paper beats rock")
        else:
            print("you lose, paper beats rock")
    elif inputU + inputB == 4:
        if inputU < inputB:
            print("You win, rock beats scissor")
        else:
            print("you lose, rock beats scissor")
    elif inputU + inputB == 5:
        if inputU > inputB:
            print("You win, scissor beats paper")
        else:
            print("you lose, scissor beats paper")


while True:

    # assign a bot who will play with user
    bot = random.randint(1, 3)

    # take user input
    user = int(input("Enter your choice (1/2/3/4) : "))

    if user == 4:
        break
    elif not 1 <= user <= 4:
        print("invalid input")
        continue

    # check condition & return game result
    main(user, bot)
