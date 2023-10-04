'''
Write a python program to check whether the number is odd or even.
Function Name: evenOdd()

Input format :
Input consists of an integer.

Output format :
Output prints whether the number is odd or even.

Sample test cases :
Input 1 :
144
Output 1 :
even
Input 2 :
121
Output 2 :
odd
'''
def evenOdd(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
 
num = int(input())       
evenOdd(num)