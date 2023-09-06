'''
In an exam, Regina has to find the smallest exact divisor of a number other than one.
Write a program to obtain a number and to find the smallest exact divisor of a number other than 1.

Input format :
Input consists of a single integer.

Output format :
The output prints a single integer which is the smallest exact divisor of the number other than 1.

Sample test cases :
Input 1 :
55

Output 1 :
5

Input 2 :
39

Output 2 :
3
'''

n=int(input())
for i in range(2,n+1):
    if n%i == 0:
        print(i)
        break