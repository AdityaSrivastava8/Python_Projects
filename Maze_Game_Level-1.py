maze = [ ['S','.','.'],
         ['#','#','.'],
         ['.','.','E'] ]

x, y = 0, 0      # Player starts at (0,0)
moves = 0        # Counts total moves made

print("=== Maze Game ===")
print("W=Up, S=Down, A=Left, D=Right, Q=Quit")
print("Reach E to Win!\n")

while True:

    # Display the maze
    for i in range(len(maze)):
        for j in range(len(maze[0])):

            # Show player position as 'P'
            if i == x and j == y:
                print("P", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

    # Show current game status
    print(f"\nCurrent Position: ({x},{y})")
    print(f"Moves: {moves}")

    # Take user input and convert to uppercase
    move = input("W/A/S/D: ").upper()

    # Quit game
    if move == 'Q':
        print("Game Over!")
        break

    # Temporary variables for next position
    nx, ny = x, y
    direction = ""

    # Determine movement direction
    if move == 'W':
        nx -= 1          # Move up
        direction = "Up"

    elif move == 'S':
        nx += 1          # Move down
        direction = "Down"

    elif move == 'A':
        ny -= 1          # Move left
        direction = "Left"

    elif move == 'D':
        ny += 1          # Move right
        direction = "Right"

    else:
        print("Invalid Input!")
        continue

    # Check if new position is inside maze boundaries
    if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):

        # Check if next cell is not a wall
        if maze[nx][ny] != '#':
            x, y = nx, ny      # Update player position
            moves += 1         # Increase move count

            print(f"Moved {direction} to ({x},{y})")

        else:
            print("Wall Hit!")

    else:
        print("Out of Bounds!")

    # Check win condition
    if maze[x][y] == 'E':
        print(f"\nYou Win in {moves} moves!")
        break


# Time Complexity:
# O(R × C) per iteration of the game loop
# because the entire maze is printed every turn.
# Here R = rows and C = columns.

# Space Complexity:
# O(1) auxiliary space
# Only a few variables (x, y, nx, ny, moves, direction)
# are used apart from the given maze.
