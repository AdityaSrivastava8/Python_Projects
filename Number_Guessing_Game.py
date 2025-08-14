import random  # Import the random module to generate random numbers

def number_guessing_game():
    print("Welcome to the Number Guessing Game!!")  # Intro message
    
    print("Select a difficulty level")  
    print("1. Easy (10 attempts)")  
    print("2. Medium (7 attempts)")  
    print("3. Hard (5 attempts)")  

    # Choose difficulty
    while True:  # TC: O(1) | SC: O(1)
        choice = input("Enter 1, 2, or 3: ")  
        if choice == "1":
            attempts = 10  # Easy mode
            break
        elif choice == "2":
            attempts = 7   # Medium mode
            break
        elif choice == "3":
            attempts = 5   # Hard mode
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")  

    # Generate secret number after difficulty is set
    secret_number = random.randint(1, 100)  # TC: O(1) | SC: O(1)
    score = 100  # Starting score

    print("\nI have chosen a number between 1 and 100. Try to guess it!")

    # Game loop
    while attempts > 0:  # TC: O(k) where k = attempts | SC: O(1)
        try:
            guess = int(input(f"Attempts left: {attempts}. Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:  # Validate guess range
            print("Guess must be between 1 and 100.")
            continue

        if guess == secret_number:  # Correct guess
            print(f"Correct!! You guessed it right!! {attempts} attempts left!")
            print(f"Your score: {score}")
            break
        elif guess < secret_number:  # Too low
            print("Too Low")
        else:  # Too high
            print("Too High")

        attempts -= 1  # Decrement attempts
        score -= 10    # Deduct points for wrong guesses

    else:  # If loop exits without a break
        print(f"Out of attempts!! The number was {secret_number}")
        print(f"Your final score: {score}")

# Replay loop (avoids recursion to prevent stack overflow)
while True:  # TC: O(m*k) where m = rounds played, k = attempts per round | SC: O(1)
    number_guessing_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!!!")
        break
