'''
Write a python program to print the sum of n numbers using looping constructs.

Input format :
Input consists of an integer 'n'.

Output format :
The output displays the sum of n numbers.

Sample test cases :
Input 1 :
10

Output 1 :
55

Input 2 :
3

Output 2 :
6
'''

'''
n=int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)
'''

n=int(input())
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    
print(sum)