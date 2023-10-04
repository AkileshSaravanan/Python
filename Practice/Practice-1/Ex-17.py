'''
Write a python function to find the Max of three numbers.

Function Name: max_of_three()

Input format :
Input consists of an integer separated by a comma.

Output format :
Output prints a maximum of three numbers.

Sample test cases :
Input 1 :
3,-7,9
Output 1 :
9
Input 2 :
5,-3,6
Output 2 :
6
'''
def max_of_three(n1,n2,n3):
    print(max(n1,n2,n3))
n1,n2,n3 = input().split(",")
max_of_three(n1,n2,n3)