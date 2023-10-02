'''
Given a list of numbers, you have to sort them in non decreasing order.

Input Format
The first line contains a single integer, N, denoting the number of integers in the list.
The next N lines contain a single integer each, denoting the elements of the list.
Output Format
Output N lines, containing one integer each, in non-decreasing order.

Constraints
1≤N≤10 
 
Sample 1:
Input
5
5
3
6
7
1

Output
1
3
5
6
7
'''

t = int(input())
a = []
for i in range(t):
    a.append(int(input()))
a.sort()
for j in range(len(a)):
    print(a[j])
