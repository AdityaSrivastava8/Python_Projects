import random  # Used to generate random selections

# List of words available for the game
words = ["python", "apple", "banana", "coding"]

# Randomly select one word from the list
word = random.choice(words)

# Stores all letters guessed by the player
guessed = []

# Number of incorrect guesses allowed
lives = 6

print("=== HANGMAN LEVEL 1 ===")

# Main game loop runs until lives become 0
while lives > 0:

    # Stores the current visible state of the word
    display = ""

    # Traverse each letter of the selected word
    for letter in word:
        if letter in guessed:
            display += letter + " "  # Show guessed letter
        else:
            display += "_ "  # Hide unguessed letter

    print("\nWord:", display)
    print("Lives:", lives)

    # If no underscores remain, the player has guessed the word
    if "_" not in display:
        print("\n🎉 You Win!")
        break

    # Take a letter as input and convert it to lowercase
    guess = input("Enter a letter: ").lower()

    # Validate input (must be exactly one character)
    if len(guess) != 1:
        print("Enter one letter only.")
        continue

    # Store the guessed letter
    guessed.append(guess)

    # Check whether the guessed letter exists in the word
    if guess not in word:
        lives -= 1  # Reduce life for wrong guess
        print("❌ Wrong!")
    else:
        print("✅ Correct!")

# Executed when all lives are lost
if lives == 0:
    print("\n💀 Game Over")
    print("Word was:", word)

# --------------------------------------------------
# Time Complexity:
# O(k × n)
# k = number of guesses made by the player
# n = length of the selected word
# Each turn traverses the whole word once.

# Space Complexity:
# O(n)
# 'guessed' and 'display' can store up to n characters.
# --------------------------------------------------
