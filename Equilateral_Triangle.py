n = 5  # Number of rows for the triangle pattern

for i in range(n):
    for j in range(i, n):  
        print(' ', end='  ')  # Prints decreasing spaces to align stars
    for y in range(i):  
        print("*", end='  ')  # Prints increasing stars on the left half
    for p in range(i + 1):  
        print("*", end='  ')  # Prints increasing stars on the right half
    print()  # Moves to the next line

# Time Complexity: O(n^2) - Nested loops iterate in a quadratic manner
# Space Complexity: O(1) - Only constant extra space is used
