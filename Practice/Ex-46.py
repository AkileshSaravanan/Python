'''
Chef has a string S with him. Chef is happy if the string contains a contiguous substring of length strictly greater than 2 in which all its characters are vowels.
Determine whether Chef is happy or not.
Note that, in english alphabet, vowels are a, e, i, o, and u.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, a string S.
Output Format
For each test case, if Chef is happy, print HAPPY else print SAD.

You may print each character of the string in uppercase or lowercase (for example, the strings hAppY, Happy, haPpY, and HAPPY will all be treated as identical).

Constraints
1≤T≤1000
3≤∣S∣≤1000, where 
S will only contain lowercase English letters.

Sample 1:
Input
4
aeiou
abxy
aebcdefghij
abcdeeafg

Output
Happy
Sad
Sad
Happy
'''
t= int(input())
for i in range(t):
    s=input()
    l=["a", "e", "i", "o", "u"]
    for i in range(len(s)):
        if s[i] in l:
            if s[i+1] in l and s[i+2] in l:
                print("Happy")
                break
    else:
        print("Sad")