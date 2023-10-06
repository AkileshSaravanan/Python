'''
A function within a function is a concept in Python where you define and call a function inside another function. This is known as a nested function or inner function.

Functions can call other functions at any level of nesting or independently.

Check the sample code given below

# Function to calculate the square of a number
def square(num):
    return num * num

# Function to calculate the square of a number and then double the result
def square_and_double(num):
    # Call the square function to calculate the square of the input number
    squared = square(num)
    # Double the squared result
    return 2 * squared

# Call the square_and_double function with the argument 3
result = square_and_double(3)

print("Result:", result)     # Output will be 'Result: 18'
Task
You are given a code in the IDE.
Check the expected output below and update the code to get the same.

Sample 1:
Input
Output
 
Greeting: Hello, Alice!
Capitalized Greeting: HELLO, ALICE!
Final Result: HELLO, ALICE!
'''