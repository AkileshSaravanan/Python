'''
Alice and Bob are playing a game of Blobby Volley. In this game, in each turn, one player is the server and the other player is the receiver. Initially, Alice is the server, and Bob is the receiver.
If the server wins the point in this turn, their score increases by 1, and they remain as the server for the next turn.
But if the receiver wins the point in this turn, their score does not increase. But they become the server in the next turn.
In other words, your score increases only when you win a point when you are the server.
Please see the Sample Inputs and Explanation for more detailed explanation.

They start with a score of 0 each, and play N turns. 
The winner of each of those hands is given to you as a string consisting of 'A's and 'B's. 
'A' denoting that Alice won that point, and 'B' denoting that Bob won that point.
Your job is the find the score of both of them after the N turns.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains one integer N — the number of turns.
The line contains a string S of length N.

Output Format
For each test case, output on a new line, two space-separated integers - Alice's final score, and Bob's final score.

Constraints
1≤T≤1000
1≤N≤1000
S consists only of the characters 'A' and 'B'.

Sample 1:
Input
4
3
AAA
4
BBBB
5
ABABB
5
BABAB

Output
3 0
0 3
1 1
0 0
'''
t=int(input())
while(t):
    n=int(input())
    s=input()
    a=0
    b=0
    c="A"
    for i in s:
        if(i=="A" and c=="A"):
           a=a+1
        elif(i=="B"and c=="B"):
           b=b+1
        elif(i=="A" and c=="B"):
           c="A"
        elif(i=="B" and c=="A"):
           c="B"
    print(a,b)
    t=t-1    