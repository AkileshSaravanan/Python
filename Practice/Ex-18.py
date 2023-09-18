'''
Write a Python function to check whether a number is in a given range. 
Here n1 and n2 have represented the range. Print inside if the number is between range otherwise print outside.

Function Name: test_range()

Input format :
The first line of the input represents the starting range n1

The second line of the input represents the ending range n2.

Output format :
Output prints whether a number is in a given range or not.

Sample test cases :
Input 1 :
100
120
111
Output 1 :
Inside

Input 2 :
10
20
25
Output 2 :
Outside
'''
def test_range():
    n1=int(input())
    n2=int(input())
    n3=int(input())
    if n3 in range(n1,n2):
        print("Inside")
    else:
        print("Outside")
test_range()