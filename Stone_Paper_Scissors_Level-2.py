# Stone Paper Scissors - Level 2
#
# Time Complexity: O(R)
# R = Number of rounds played (Maximum 5 per match)
#
# Space Complexity: O(1)
# Only a fixed number of variables are used.

import random  # Used for computer's random choice

# List containing all possible choices
choices = ["stone", "paper", "scissors"]

print("===== STONE PAPER SCISSORS : LEVEL 2 =====")

# Main loop allows the player to play multiple matches
while True:

    # Initialize scores
    user_score = 0
    computer_score = 0
    draws = 0

    # Total number of rounds
    total_rounds = 5

    # Loop through each round
    for round_number in range(1, total_rounds + 1):

        print("\n==============================")
        print("Round", round_number)
        print("==============================")

        # Take valid user input
        while True:

            user = input("Enter Stone, Paper, or Scissors: ").lower()

            # Input validation
            if user in choices:
                break

            print("❌ Invalid choice! Please enter Stone, Paper, or Scissors.")

        # Computer randomly chooses
        computer = random.choice(choices)

        print("You Chose      :", user.capitalize())
        print("Computer Chose :", computer.capitalize())

        # Check draw
        if user == computer:

            print("🤝 It's a Draw!")

            draws += 1

        # Check if user wins
        elif (
            (user == "stone" and computer == "scissors") or
            (user == "paper" and computer == "stone") or
            (user == "scissors" and computer == "paper")
        ):

            print("🎉 You Win This Round!")

            user_score += 1

        # Otherwise computer wins
        else:

            print("💻 Computer Wins This Round!")

            computer_score += 1

        # Display live scoreboard
        print("\nCurrent Score")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("Draws    :", draws)

    # ==========================
    # MATCH RESULT
    # ==========================

    print("\n===================================")
    print("FINAL RESULT")
    print("===================================")

    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)
    print("Draws          :", draws)

    if user_score > computer_score:

        print("\n🏆 Congratulations!")
        print("You Won the Match!")

    elif computer_score > user_score:

        print("\n💀 Computer Won the Match!")

    else:

        print("\n🤝 The Match Ended in a Draw!")

    # Ask the user if they want to play another match
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":

        print("\n👋 Thanks for playing!")
        break

