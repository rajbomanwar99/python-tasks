# Task 2: Using the Math Module for Calculations

import math

# Ask the user for a number
number = float(input("Enter a number: "))

# Calculate using the math module
sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)  # number is treated as radians

# Display the results
print(f"\nResults for number {number}:")
print(f"Square root: {sqrt_result}")
print(f"Natural logarithm (ln): {log_result}")
print(f"Sine (in radians): {sine_result}")