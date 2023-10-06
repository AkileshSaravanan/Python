'''
Note that there is a difference between Parameters and Arguments - actual values passed to a function.
Check the code template below

a, b are Parameters inside the function
A, B are Arguments passed to the function
def add_numbers(a, b):
    return a + b

# Calling the function with arguments
A = 5
B = 3
result = add_numbers(A, B)
print("Sum:", result)
Task
The code given in the IDE is incorrect.
Can you debug the code to give the correct output?
Check the input and expected output below.

Sample 1:
Input

Output
Hello, Alice!
'''
def greet(name):
    print("Hello, " + name + "!")

name = "Alice"
greet(name)