#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    - n (int): The non-negative integer for which the factorial is calculated.

    Returns:
    - int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input number from the command-line argument
input_number = int(sys.argv[1])

# Calculate the factorial of the input number using the factorial function
factorial_result = factorial(input_number)

# Print the calculated factorial
print(factorial_result)