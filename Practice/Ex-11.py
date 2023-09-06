'''
Write a program to obtain m and n and print "True" if m is greater than n, else print "False".

Input format :
The first line of the input consists of an integer, n.
The second line of the input consists of an integer, m.

Output format :
The output prints "True" if m is greater than n. Otherwise prints "False".

Sample test cases :
Input 1 :
15
78

Output 1 :
True

Input 2 :
45
13

Output 2 :
False
'''
n=int(input())
m=int(input())
if n < m:
	print("True")
else:
	print("False")