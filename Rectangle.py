n = 5  # Size of the square

for i in range(n):  # Outer loop runs 'n' times -> O(n)
    for j in range(n):  # Inner loop runs 'n' times for each outer iteration -> Total O(n^2)
        print("*", end='    ')  # Printing each star, no extra space except loop variables
    print()  # Move to next line after printing each row

# TC: O(n^2) -> Nested loops each running 'n' times
# SC: O(1)   -> Constant extra space (only loop counters)
