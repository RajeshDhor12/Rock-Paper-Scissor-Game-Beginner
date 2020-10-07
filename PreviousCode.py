import random

print("Rock-Paper-Scissor Game\n 1.Rock \n 2. Paper \n 3.Scissor\n 4.To Stop the Game")

while True:
    # create a list of play options
    options = ["1", "2", "3"]

    # assign a bot who will play with user
    bot = random.choice(options)

    # take user input
    user = input("Enter your choice (1/2/3/4) : ")

    # check condition & return game result
    if user == bot:
        print("Tie!")

    # if user choose 1.rock as input
    elif user == "1":
        if bot == "2":
            print("You Lose! Computer select -> Paper")
        else:
            print("You Win! Computer select -> Scissor")

    # if user choose 2.paper as input
    elif user == "2":
        if bot == "3":
            print("You Lose! Computer select -> Scissor")
        else:
            print("You Win! Computer select -> Rock")

    # if user choose 3.scissor as input
    elif user == "3":
        if bot == "1":
            print("You Lose! Computer select -> Rock")
        else:
            print("You Win! Computer select -> Paper")

    # if user choose 4.to quit the game as input
    elif user == "4":
        print("Game Over!!!!")
        exit()

    # if user choose any invalid input
    else:
        print("Invalid Input.Check your input number[1-4]!")
