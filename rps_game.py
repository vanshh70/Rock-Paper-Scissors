import random

choices = ['rock', 'paper', 'scissors']

# Get user input
user_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Decide the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == 'rock' and computer_choice == 'scissors') or
    (user_choice == 'paper' and computer_choice == 'rock') or
    (user_choice == 'scissors' and computer_choice == 'paper')
):
    print("You win!")
elif user_choice in choices:
    print("You lose!")
else:
    print("Invalid choice!")
