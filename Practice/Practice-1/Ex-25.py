'''
Your task is very simple: given two integers A and B, write a program to add these two numbers and output the sum.

Input Format
The first line contains an integer T, the total number of test cases.
Then follow T lines, each line contains two integers, A and B.
Output Format
For each test case, add A and B and display the sum in a new line.

Constraints
1≤T≤1000
0≤A,B≤10000

Sample 1:
Input
3
1 2
100 200
10 40

Output
3
300
50
'''
t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(a+b)