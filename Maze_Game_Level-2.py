maze = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '#', 'E']
]

# Space Complexity: O(rows × cols)
# Reason: The maze itself stores rows × cols cells.

player_x, player_y = 0, 0
moves = 0

print("=== LEVEL 2 MAZE GAME ===")
print("W = Up")
print("S = Down")
print("A = Left")
print("D = Right")
print("Q = Quit")
print("Reach E to Win!\n")

while True:

    # Display Maze
    # Time Complexity: O(rows × cols)
    # Reason: Every cell of the maze is printed once.
    for i in range(len(maze)):
        for j in range(len(maze[0])):

            if (i, j) == (player_x, player_y):
                print("P", end=" ")
            else:
                print(maze[i][j], end=" ")

        print()

    # Display Status
    print(f"\nCurrent Position: ({player_x},{player_y})")
    print(f"Moves: {moves}")

    # Input
    move = input("Enter Move (W/A/S/D): ").upper()

    # Quit Game
    if move == 'Q':
        print("\nGame Over!")
        break

    nx, ny = player_x, player_y
    direction = ""

    # Movement Logic
    # Time Complexity: O(1)
    # Reason: Only a few comparisons and assignments are performed.
    if move == 'W':
        nx -= 1
        direction = "Up"

    elif move == 'S':
        nx += 1
        direction = "Down"

    elif move == 'A':
        ny -= 1
        direction = "Left"

    elif move == 'D':
        ny += 1
        direction = "Right"

    else:
        print("\nInvalid Input!")
        continue

    # Boundary Check
    # Time Complexity: O(1)
    if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):

        # Wall Check
        # Time Complexity: O(1)
        if maze[nx][ny] != '#':

            player_x, player_y = nx, ny
            moves += 1

            print(f"\nMoved {direction}")
            print(f"New Position: ({player_x},{player_y})")

        else:
            print("\n🚫 Wall Hit!")

    else:
        print("\n🚫 Out of Bounds!")

    # Win Condition
    # Time Complexity: O(1)
    if maze[player_x][player_y] == 'E':

        print("\n🎉 CONGRATULATIONS!")
        print("You Escaped the Maze!")
        print(f"Total Moves: {moves}")

        break

# ----------------------------------------------------
# Overall Time Complexity:
# O(rows × cols) per game iteration
# because displaying the maze visits every cell once.
#
# If the player makes M moves before winning or quitting,
# the total time complexity becomes:
# O(M × rows × cols)
#
# Overall Space Complexity:
# O(rows × cols)
# because the maze occupies rows × cols memory.
# The additional variables (player_x, player_y, nx, ny,
# moves, direction) require only O(1) extra space.
# ----------------------------------------------------
