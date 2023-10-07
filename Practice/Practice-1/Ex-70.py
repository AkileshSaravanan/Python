'''
Let us now solve some programming problems. Note that

In the IDE - the '#' - comments will give you hints about what you need to do
The Solution tab also has '#' - comments which give you helpful information
Task
Write a program in the IDE which does the following

Accepts the count of test cases - 
�
t - in the 1st line
The only line of each test case consists of an integer N
You need to generate the following output - Change the sign of N.

Sample 1:
Input
5
1
2
3
-4
-5

Output
-1
-2
-3
4
5
'''
t = int(input())        
#run a loop to accept 't' inputs
for i in range(t):      
    #accept 1 integer on the 1st line of each test case
    N = int(input())        
    #output the negative integer - i.e. (-N)
    print(-N)