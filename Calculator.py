try:
    number1 = input("Enter the num: ")           # Take first number as string input
    num1 = int(number1)                          # Convert to integer (O(1))

    sign = input("Enter the sign: ")              # Take arithmetic operator input (O(1))

    number2 = input("Enter the number: ")         # Take second number as string input
    num2 = int(number2)                          # Convert to integer (O(1))

    if sign == '+':                               # Check if operator is addition
        print("Your result is " + str(num1 + num2))   # Addition (O(1))
    elif sign == '-':                             # Check if operator is subtraction
        print("Your result is " + str(num1 - num2))   # Subtraction (O(1))
    elif sign == '*':                             # Check if operator is multiplication
        print("Your result is " + str(num1 * num2))   # Multiplication (O(1))
    elif sign == '/':                             # Check if operator is division
        print("Your result is " + str(num1 / num2))   # Division (O(1))
    else:
        print("Please enter +, -, *, or /")       # Invalid operator case (O(1))

except ValueError:                                # Handles invalid integer inputs
    print("Invalid input! Please enter valid numbers.")  
except ZeroDivisionError:                         # Handles division by zero
    print("Division by zero is not allowed.")     
except Exception as e:                            # Handles any other unexpected errors
    print("An error occurred:", e)

# Time Complexity: O(1) -> All operations are constant time arithmetic and comparisons
# Space Complexity: O(1) -> Only a fixed number of variables are used
