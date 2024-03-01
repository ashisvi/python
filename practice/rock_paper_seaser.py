import random


def start_game():
    choices = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock/paper/scissor): ").lower()

    print(f"\nComputer's choice: {computer_choice}")
    print(f"Your choice: {user_choice}")

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper or scissor")
    elif user_choice == computer_choice:
        print("Game draw!")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'scissor' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")


start_game()
