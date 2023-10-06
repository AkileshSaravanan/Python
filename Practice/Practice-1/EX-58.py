'''
Let us solve a simple problem to help us understand the importance of functions.

Task
Your are given 3 lines of input.
Each line consists of 2 space separated integers - A and B
Check the sample output below to understand this problem statement better.

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
for _ in range(3):
    A, B = map(int, input().split())
    C = A**2 + B**3 + (A**2 + B**3)**2 + (A**2 + B**3)**3
    print(C)