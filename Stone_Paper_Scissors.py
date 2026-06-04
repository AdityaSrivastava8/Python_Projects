import random  # Used to let the computer make a random choice

# List of possible choices
choices = ["stone", "paper", "scissors"]

# Take input from the user
user = input("Enter stone, paper, or scissors: ").lower()

# Computer randomly selects one choice from the list
computer = random.choice(choices)

# Display both choices
print("You chose:", user)
print("Computer chose:", computer)

# Check for a draw
if user == computer:
    print("It's a draw!")

# User wins if:
# Stone beats scissors
# Paper beats stone
# Scissors beats paper
elif (
    (user == "stone" and computer == "scissors") or
    (user == "paper" and computer == "stone") or
    (user == "scissors" and computer == "paper")
):
    print("You win!")

# If it's not a draw and user didn't win, computer wins
else:
    print("Computer wins!")

# Time Complexity: O(1)
# Explanation: The program performs a fixed number of operations
# regardless of the user's input size.

# Space Complexity: O(1)
# Explanation: Only a few variables (choices, user, computer) are used,
# and their size does not grow with input.
