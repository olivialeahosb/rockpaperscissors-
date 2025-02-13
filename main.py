import random

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    """Gets the user's choice and ensures it's valid."""
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return f"You win! Computer chose {computer_choice}."
    else:
        return f"You lose! Computer chose {computer_choice}."

def play_game():
    """Function that plays a single round of the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

def play_again():
    """Asks the user if they want to play again."""
    play_again_choice = input("Do you want to play again? (yes or no): ").lower()
    return play_again_choice == "yes"

# Main loop to allow multiple rounds
def main():
    """Main function that loops the game and allows playing multiple rounds."""
    while True:
        play_game()
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()



