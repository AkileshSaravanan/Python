'''
Multiplication Table
Nive wants to learn multiplication tables. 
Write a program to print the multiplication table of a given number up to some end value given by the user.

Input format :
The first line of the input consists of a number. The number of which you want to print its multiplication table.
The second line of the input is the end value. The number up to which you want to print the table.

Output format :
The output prints the multiplication table of the given number up to the end value.

Sample test cases :
Input 1 :
5
12

Output 1 :
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50
11 x 5 = 55
12 x 5 = 60
'''
t=int(input())
n=int(input())
for i in range(1,n+1):
    s = t*i
    print(i,"x",t,"=",s)