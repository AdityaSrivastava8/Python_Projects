import random

# =====================================================
# SNAKE GAME - LEVEL 1
# =====================================================
#
# Time Complexity:
# O(R × C)
# R = Number of rows
# C = Number of columns
# The board is redrawn every move.
#
# Space Complexity:
# O(R × C)
# Space is used to store the game board.
# =====================================================

# Board size
ROWS = 10
COLS = 10

# Snake starts in the center
snake_row = ROWS // 2
snake_col = COLS // 2

# Initial score
score = 0

# Generate food at a random position
food_row = random.randint(0, ROWS - 1)
food_col = random.randint(0, COLS - 1)

print("===== SNAKE GAME : LEVEL 1 =====")
print("Controls: W = Up, S = Down, A = Left, D = Right")

# Main game loop
while True:

    # Create an empty board
    board = []

    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(".")
        board.append(row)

    # Place snake
    board[snake_row][snake_col] = "S"

    # Place food
    board[food_row][food_col] = "F"

    # Display board
    print("\nScore:", score)

    for row in board:
        print(" ".join(row))

    # Take player input
    move = input("\nMove (W/A/S/D): ").lower()

    # Move snake
    if move == "w":
        snake_row -= 1

    elif move == "s":
        snake_row += 1

    elif move == "a":
        snake_col -= 1

    elif move == "d":
        snake_col += 1

    else:
        print("Invalid move!")
        continue

    # Check wall collision
    if (
        snake_row < 0 or
        snake_row >= ROWS or
        snake_col < 0 or
        snake_col >= COLS
    ):
        print("\n💥 GAME OVER!")
        print("Final Score:", score)
        break

    # Check if food is eaten
    if (
        snake_row == food_row and
        snake_col == food_col
    ):
        score += 1

        # Generate new food
        while True:
            food_row = random.randint(0, ROWS - 1)
            food_col = random.randint(0, COLS - 1)

            if (
                food_row != snake_row or
                food_col != snake_col
            ):
                break

        print("🍎 Food Eaten!")
