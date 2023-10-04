'''
For encoding an even-length binary string into a sequence of A, T, C, and G, we iterate from left to right and replace the characters as follows:
00 is replaced with A
01 is replaced with T
10 is replaced with C
11 is replaced with G
Given a binary string S of length N (N is even), find the encoded sequence.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains two lines of input.
First line contains a single integer N, the length of the sequence.
Second line contains binary string S of length N.
Output Format
For each test case, output in a single line the encoded sequence.

Note: Output is case-sensitive.

Constraints
1≤T≤100
2≤N≤10 
N is even.
Sum of N over all test cases is at most 10^3 .
S contains only characters 0 and 1.

Sample 1:
Input
4
2
00
4
0011
6
101010
4
1001

Output
A
AG
CCC
CT
'''
t=int(input())
for i in range(t):
    N = int(input())
    S = input()
    for i in range(0,N,2):
        if S[i] == '0' and S[i + 1] == '0':
            print("A", end="")
        if S[i] == '0' and S[i + 1] == '1':
            print("T", end="")
        if S[i] == '1' and S[i + 1] == '0':
            print("C", end="")
        if S[i] == '1' and S[i + 1] == '1':
            print("G", end="")
    print()    
        