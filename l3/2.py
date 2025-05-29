import random

def jugar():
    while True:
        users_pick = input("Hello, and welcome to Rock, Paper, Scissors. Please choose an item (rock, paper, scissors): ").lower()
        options = ["paper", "rock", "scissors"]
        
        if users_pick not in options:
            print("Invalid choice, please try again.")
            continue
        
        computer = random.choice(options)

        if users_pick == computer:
            print(f"Both sides have chosen {users_pick}. It's a tie.")
        elif users_pick == "scissors":
            if computer == "rock":
                print("Rock smashed scissors, you have lost.")
            else:
                print("Scissors cut paper, you have won!")
        elif users_pick == "rock":
            if computer == "paper":
                print("Paper covers rock, you have lost.")
            else:
                print("Rock smashed scissors, you have won!")
        elif users_pick == "paper":
            if computer == "rock":
                print("Paper covers rock, you have won!")
            else:
                print("Scissors cut paper, you have lost.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

jugar()