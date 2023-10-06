'''
Functions allow you to break down a complex program into smaller, manageable modules.
Each function can represent a specific task or functionality.
Once defined, functions can be reused in different parts of the program or even in different programs, promoting code reuse and saving development time.

Look at the code in the IDE for the previous problem which highlights the implementation of functions.
Review the code and click on Submit to proceed.

Sample 1:
Input
3 5
2 7
4 1

Output
2424194
41902679
5219
'''
def calculate(a, b):
    result = a**2 + b**3 + (a**2 + b**3)**2 + (a**2 + b**3)**3
    return result

for _ in range(3):
    A, B = map(int, input().split())
    result = calculate(A, B)
    print (result)