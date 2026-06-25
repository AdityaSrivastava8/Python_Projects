# Infection Survival - Level 1
#
# Time Complexity: O(D)
# D = Number of days survived (5 in this game)
# We perform constant work for each day.
#
# Space Complexity: O(1)
# Only a few variables (health, food, day, choice) are used,
# regardless of the number of days.

# Player starts with full health
health = 100

# Initial food supply
food = 3

# Starting day
day = 1

print("===== INFECTION SURVIVAL : LEVEL 1 =====")

# Main game loop runs until:
# 1. Player survives 5 days OR
# 2. Health becomes 0 or less
while day <= 5 and health > 0:

    print("\n-------------------------")

    # Display current game status
    print("Day:", day)
    print("Health:", health)
    print("Food:", food)

    # Show available actions
    print("\nChoose an action")
    print("1. Search Food")
    print("2. Rest")

    # Take player's choice
    choice = input("Enter choice: ")

    # Option 1: Search for food
    if choice == "1":

        print("\n🍎 You searched for food.")

        # Player finds 2 food
        food += 2

        print("Found 2 food!")

    # Option 2: Rest
    elif choice == "2":

        print("\n😴 You rested.")

        # Increase health by 10
        health += 10

        # Health cannot exceed 100
        if health > 100:
            health = 100

        print("Health increased.")

    # Invalid input handling
    else:

        print("Invalid choice.")

        # Restart current day without penalty
        continue

    # Daily food consumption
    food -= 1

    # If food becomes negative,
    # player loses health due to starvation
    if food < 0:

        health -= 20

        print("\n⚠ No food available!")
        print("You lost 20 health.")

    # Move to next day
    day += 1

# ==========================
# FINAL RESULT
# ==========================

# If health is still above 0,
# player successfully survived
if health > 0:

    print("\n🏆 CONGRATULATIONS!")
    print("You survived 5 days.")

# Otherwise player dies
else:

    print("\n💀 GAME OVER")
    print("You did not survive.")
