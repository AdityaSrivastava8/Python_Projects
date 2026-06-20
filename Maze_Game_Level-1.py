# Time Complexity:
# O(k), where k = number of moves entered by the player.
# Each iteration of the loop takes O(1) time.

# Auxiliary Space Complexity:
# O(1), since only a few extra variables (x, y, nx, ny, move)
# are used regardless of maze size.

# 3x3 maze:
# S = Start
# E = End
# # = Wall
# . = Free path
maze = [
    ['S', '.', '.'],
    ['#', '#', '.'],
    ['.', '.', 'E']
]

# Player starts at position (0, 0)
x, y = 0, 0

# Keep taking moves until the player reaches E
while True:
    # Take user input and convert it to uppercase
    move = input("W/A/S/D: ").upper()

    # Store current position temporarily
    nx, ny = x, y

    # Update next position based on the move
    if move == 'W':      # Move Up
        nx -= 1
    elif move == 'S':    # Move Down
        nx += 1
    elif move == 'A':    # Move Left
        ny -= 1
    elif move == 'D':    # Move Right
        ny += 1

    # Check if the new position is inside maze boundaries
    # Time Complexity: O(1)
    if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):

        # Check if the new position is not a wall
        # Time Complexity: O(1)
        if maze[nx][ny] != '#':
            x, y = nx, ny   # Move player

    # Check if player has reached the end cell
    # Time Complexity: O(1)
    if maze[x][y] == 'E':
        print("You Win!")
        break
