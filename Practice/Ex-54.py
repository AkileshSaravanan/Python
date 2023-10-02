'''
In a class of N students, a class test was held. It is also known that the scores of all students were distinct.
A student passes the test if their score is strictly greater than the passing mark. 
Given that exactly X students pass in the test, find the maximum value of the passing mark of the test.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains two space-separated integers N and X — the number of students in the class and the number of students that passed in the test.

Output Format
For each test case, output on a new line, the maximum value of the passing mark of the test.

Constraints
1≤T≤100
1≤N≤100
1≤X≤N

Sample 1:
Input
3
2 2
5 1
4 1
5 1 7 4
4 3
15 70 100 31

Output
0
6
30
'''
import sys
# Main function
def main():
    # Taking input for the number of test cases
    T = int(input())    
    # Running the loop for each test case
    for i in range(T):
        # Taking input for N and X
        N, X = map(int, input().split())        
        # Taking input for the array A
        A = list(map(int, input().split()))        
        # Sorting the array A
        A.sort()        
        # Printing the result
        print(A[N - X] - 1)
# Calling the main function
if __name__ == "__main__":
    main()