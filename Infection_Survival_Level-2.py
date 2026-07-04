# Infection Survival - Level 2
#
# Time Complexity: O(D)
# D = Number of days survived.
# Each day performs a constant amount of work.
#
# Space Complexity: O(1)
# Only fixed-size variables are used.

import random

# Player stats
health = 100
food = 3
infection = 0
day = 1

print("===== INFECTION SURVIVAL : LEVEL 2 =====")

# Main game loop
while day <= 7 and health > 0 and infection < 100:

    print("\n-------------------------")
    print("Day:", day)
    print("Health:", health)
    print("Food:", food)
    print("Infection:", infection, "%")

    # Display menu
    print("\nChoose an action")
    print("1. Search Food")
    print("2. Rest")
    print("3. Search Medicine")

    choice = input("Enter choice: ")

    # ==========================
    # SEARCH FOOD
    # ==========================
    if choice == "1":

        print("\n🍎 Searching for food...")

        # 50% chance of zombie encounter
        if random.randint(1, 2) == 1:

            print("🧟 A zombie appeared!")

            action = input("Fight or Run? ").lower()

            if action == "fight":

                # Random fight result
                if random.randint(1, 2) == 1:

                    print("⚔️ You defeated the zombie!")
                    food += 2

                else:

                    print("🩸 Zombie bit you!")

                    health -= 15
                    infection += 20

            elif action == "run":

                print("🏃 You escaped safely!")

            else:

                print("Confused! Zombie attacked.")

                health -= 10

        else:

            print("🍎 Found 2 food!")
            food += 2

    # ==========================
    # REST
    # ==========================
    elif choice == "2":

        print("\n😴 Resting...")

        health += 10

        # Health cap
        if health > 100:
            health = 100

        print("Health increased.")

    # ==========================
    # SEARCH MEDICINE
    # ==========================
    elif choice == "3":

        print("\n💊 Searching for medicine...")

        # Random outcome
        if random.randint(1, 2) == 1:

            print("Found medicine!")

            infection -= 15

            if infection < 0:
                infection = 0

        else:

            print("Nothing found.")

    # ==========================
    # INVALID INPUT
    # ==========================
    else:

        print("Invalid choice.")
        continue

    # Daily food consumption
    food -= 1

    # Starvation penalty
    if food < 0:

        print("\n⚠️ No food available!")

        health -= 20

    # Infection naturally worsens each day
    infection += 5

    # Next day
    day += 1

# ==========================
# FINAL RESULT
# ==========================

if infection >= 100:

    print("\n☣️ Infection took over!")
    print("💀 GAME OVER")

elif health <= 0:

    print("\n💀 You died.")

elif day > 7:

    print("\n🏆 CONGRATULATIONS!")
    print("You survived 7 days!")
