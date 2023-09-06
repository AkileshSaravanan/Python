'''
Write a program to print the series in descending order from the given value of n by using for loop.
Example:
Input:
4

Output:
4 3 2 1

Input format :
Input consists of an integer.

Output format :
The output displays the series till the nth term.

Refer sample input and output for better understanding.

Sample test cases :
Input 1 :
5

Output 1 :
5 4 3 2 1 

Input 2 :
10

Output 2 :
10 9 8 7 6 5 4 3 2 1 
'''
n=int(input())
for i in range(n,0,-1):
    print(i,end =' ')