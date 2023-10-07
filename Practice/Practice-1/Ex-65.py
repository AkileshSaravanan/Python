'''
In the previous problem - we wrote the program to accept 5 inputs on 5 separate lines.

What will we do if we expect 100 inputs or test cases?
What about 100,000 inputs or test cases?
Task
Lets solve a simple problem.
Write a program in the IDE which does the following

Accepts the count of test cases - t - as an integer input given in the 1st line.
This is followed by t lines - Each line contains an integer N
For each test cases, prints out the integer N to console on a separate line (our Input mirror problem)

Sample 1:
Input
3
1
22
33

Output
1
22
33
'''
t = int(input())
#Run a loop to accept 't' inputs
for i in range(t):     
    #accept an integer N in each test case
    N = int(input())         
    #output the number mirror for each test case
    print(N)           
