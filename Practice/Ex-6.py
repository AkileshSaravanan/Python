'''
Ashok is so keen on programming.
Today his professor taught him about "Looping Constructs" and gave him a task to write a python program to print natural numbers starting from 0 to n. 
Kindly help him to write code for the same.

Input format :
Input consists of an integer 'n'.

Output format :
The output prints the n natural numbers.

Sample test cases :
Input 1 :
10

Output 1 :
0 1 2 3 4 5 6 7 8 9 10 
'''

n=int(input())
for i in range(0,n+1):
    print(i,end=' ')