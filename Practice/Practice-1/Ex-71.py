'''
Write a program in the IDE which does the following

Accepts the count of test cases - t - in the 1st line
First line of each test case consists of a string S
You need to perform the following operation
Create a variable X which contains the string S concatenated with the string S
Output X for each test case

Sample 1:
Input
3
ab
bc
cd

Output
abab
bcbc
cdcd
'''
t = int(input())
for i in range(t):
    S = input()
    #create a variable X which stores the value of string S concatenated with itself
    X = S + S           
    #output the variable X
    print(X)