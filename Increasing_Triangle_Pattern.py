n = 5  # Number of rows

for i in range(n):  # Outer loop runs 'n' times -> O(n)
    for j in range(i + 1):  # Inner loop runs (i+1) times -> Total O(n^2)
        print("*", end='  ')  # Printing each star, no extra space used except loop variables
    print()  # Move to the next line after each row

# TC: O(n^2) -> Nested loops
# SC: O(1)  -> Constant extra space (only loop counters)
