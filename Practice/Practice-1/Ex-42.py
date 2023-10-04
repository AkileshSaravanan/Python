'''
In Chefland, a valid phone number consists of 5 digits with no leading zeros.
For example,98765,10000, and 71023 are valid phone numbers while 04123,9231, and 872310 are not.
Chef went to a store and purchased N items, where the cost of each item is X.
Find whether the total bill is equivalent to a valid phone number.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers N and X — the number of items Chef bought and the cost per item.
Output Format
For each test case, output on a new line, YES, if the total bill is equivalent to a valid phone number and NO otherwise.
Each character of the output may be printed in either uppercase or lowercase. That is, the strings NO, no, nO, and No will be treated as equivalent.

Constraints
1≤T≤100
1≤N,X≤1000

Sample 1:
Input
4
25 785
402 11
100 100
333 333

Output
YES
NO
YES
NO
'''
t= int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = n*x 
    if(a>=10000 and a<=99999):
        print("Yes")
    else:
        print("No")