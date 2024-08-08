import random
# Define possible choices
choices=["rock", "paper", "scissors"]
# Initialize scores
user_score = 0
computer_score = 0
while True:
    # Prompt the user to choose rock, paper, or scissors
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    # Display choices and result
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)
    print(f"Score - You: {user_score}, Computer: {computer_score}")
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Thank you for playing!")
