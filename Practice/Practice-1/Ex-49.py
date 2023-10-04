'''
Alice and Bob recently got into running, and decided to compare how much they ran on different days.
On each day,
Alice is unhappy if Bob ran strictly more than twice her distance, and happy otherwise.
Similarly, Bob is unhappy if Alice ran strictly more than twice his distance, and happy otherwise.
For example, on a given day
If Alice ran 200 meters and Bob ran 500, Alice would be unhappy but Bob would be happy.
If Alice ran 500 meters and Bob ran 240, Alice would be happy and Bob would be unhappy.
If Alice ran 300 meters and Bob ran 500, both Alice and Bob would be happy.
On how many of the N days were both Alice and Bob happy?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three lines of input.
The first line of each test case contains a single integer N — the number of days.

Output Format
For each test case, output on a new line the number of days when both Alice and Bob were happy.

Constraints
1≤T≤1000
1≤N≤100
 
Sample 1:
Input
4
3
100 200 300
300 200 100
4
1000 1000 1000 1000
400 500 600 1200
4
800 399 1400 532
2053 2300 3400 23
5
800 850 900 950 1000
600 800 1000 1200 1400

Output
1
3
0
5
'''
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        count = 0
        for k in range(n):
            if 2 * a[k] >= b[k] and a[k] <= 2 * b[k]:
                count += 1
        print(count)
        t -= 1

if __name__ == "__main__":
    main()