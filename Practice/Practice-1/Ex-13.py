'''
Write a program to find the greatest of two numbers. if A is greater than B means print Yes, otherwise print No.

Input format :
The first line of the input consists of an integer 'A'.
The second line of the input consists of an integer 'B'.

Output format :
The output prints Yes if A is greater than B. Otherwise prints No.

Sample test cases :
Input 1 :
7
8

Output 1 :
No

Input 2 :
9
8

Output 2 :
Yes
'''
A=int(input())
B=int(input())
if(A>B):
    print("Yes")
else:
    print("No")