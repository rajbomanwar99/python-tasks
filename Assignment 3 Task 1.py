# Task 1: Calculate Factorial Using a Function

# Define the factorial function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
sample_number = 5
fact = factorial(sample_number)

# Display the result
print(f"The factorial of {sample_number} is: {fact}")