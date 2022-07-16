import random
while True:
    choices=["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player=input("rock , paper or scissors?: ").lower()

    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("tie")
    elif player == "rock":
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("player win")
        elif computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("player win")
        else:
            print("computer:", computer)
            print("player:", player)
            print("tie")
    elif player == "paper":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("computer win")
        elif computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("computer win")
        else:
            print("computer:", computer)
            print("player:", player)
            print("tie")
    elif player == "scissors":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("computer win")
        elif computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("player win")
        else:
            print("computer:", computer)
            print("player:", player)
            print("tie")

    play_again = input("Play again ? yes/no")
    if play_again != "yes":
        break
print("bye")