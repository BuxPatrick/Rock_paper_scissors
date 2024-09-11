import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# Ask for the number of rounds before starting the game loop
rounds = int(input("Type in the number of rounds that you want: "))

while user_wins + computer_wins < rounds:
    user_agreement = input("Do you want to play rock/paper/scissors?\nIf 'Yes' press Y or Q to quit game ").lower()
    if user_agreement == "q":
        print("Sorry to see you go")
        quit()

    if user_agreement not in ["y", "q"]:
        print("Type in 'Y' to play or 'Q' to quit ")
        continue

    if user_agreement == "y":
        user_selection = input("Type in rock, paper or scissors: ").lower()

        if user_selection not in options:
            print("Invalid selection!")
            continue

        random_number = random.randint(0, 2)
        computer_choice = options[random_number]
        print("Computer chose", computer_choice + ".")

        if user_selection == "rock" and computer_choice == "scissors":
            print("You won!")
            user_wins += 1
        elif user_selection == "paper" and computer_choice == "rock":
            print("You won!")
            user_wins += 1
        elif user_selection == "scissors" and computer_choice == "paper":
            print("You won!")
            user_wins += 1
        elif user_selection == computer_choice:
            print("Tie!")
        else:
            print("You lost!")
            computer_wins += 1

if user_wins == computer_wins:
    print("It's a tie!")
elif user_wins > computer_wins:
    print(f":) Congratulations, you beat the computer by {user_wins - computer_wins} point(s) out of {rounds} rounds")
else:
    print(f":( Sorry, you lost by {computer_wins - user_wins} point(s) out of {rounds} rounds")

print("Goodbye!")
