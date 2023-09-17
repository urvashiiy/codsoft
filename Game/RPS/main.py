import random

options = ("rock","paper","scissor")
playing = True

userscore=0
computerscore=0
i=1

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
         player = input("Enter a choice (rock, paper, scissors): ")
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if computer == player:
        print("It's a Tie")
        
    elif player == "rock" and computer == "scissor":
        print("You win")
        
    elif player == "scissor" and computer == "paper":
        print("You win")

    elif player == "paper" and computer == "scissor":
        print("You win")

    elif player == "paper" and computer == "scissor":
        print("You win")
    else:
        print("You lose")
        
    if not input("play_again? (y/n): ").lower() == "y":
        playing = False
    
print("Thanks for playing! Bye Bye")
