'''
Write a program to find a particular number is a positive number or a negative number or zero.

Input format :
Input consists of an integer.

Output format :
The output displays whether the particular number is positive or negative or zero.

Sample test cases :
Input 1 :
6

Output 1 :
Positive number

Input 2 :
0

Output 2 :
Zero

Input 3 :
-8

Output 3 :
Negative number
'''
n=int(input())
if(n>0):
    print("Positive number")
elif(n==0):
    print("Zero")
else:
    print("Negative Number")