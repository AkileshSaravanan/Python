'''
Andrew likes meatballs very much.
He has N plates of meatballs, here the ith plate contains Pi meatballs. 
You need to find the minimal number of plates Andrew needs to take to his trip to Las Vegas, if he wants to eat there at least M meatballs. 
Note that each plate is already packed, i.e. he cannot change the amount of meatballs on any plate.

Input
The first line of the input contains an integer T, denoting the number of test cases. 
The description of T test cases follows. The first line of each test case contains two space-separated integers N and M. 
The second line contains N space-separated integers P1, P2, ..., PN.

Output
For each test case, output an integer, denoting the minimum number of plates. 
If it's impossible to take at least M meatballs, print -1.

Constraints
1 ≤ T ≤ 7777
1 ≤ N ≤ 7
1 ≤ M, Pi ≤ 1018

Sample 1:
Input
1
4 7
1 2 3 4

Output
2
'''

def main():
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())  # Read n and m from a single line
        p = list(map(int, input().split()))  # Read the list of integers from a single line
        p.sort()
        s = 0
        flag = 1
        for j in range(n - 1, -1, -1):
            s += p[j]
            if s >= m:
                flag = 0
                print(n - j)
                break
        if flag == 1:
            print(-1)
        t -= 1

if __name__ == "__main__":
    main()
