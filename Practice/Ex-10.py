'''
The Event Organizing Company "Buzzcraft" focuses on event management in a way that creates a win-win situation for all involved stakeholders. 
Buzzcraft doesn't look at building one-time associations with clients, instead, aims at creating long-lasting collaborations that will span years to come. 
This goal of the company has helped them evolve and expand big with more workforces within a notable time.
The number of employees of the company from the start day of their journey till now is recorded sensibly and it seemed to have followed a specific series like 20, 60, 104, 152, 204,…….

Write a program that takes an integer N as the input and will output the series till the Nth term.

Input format :
The input consists of an integer N.

Output format :
The output prints the series till the Nth term, each separated by a comma.

Refer to the sample output for formatting specifications.

Sample test cases :
Input 1 :
5

Output 1 :
20 60 104 152 204 

Input 2 :
10

Output 2 :
20 60 104 152 204 260 320 384 452 524 
'''

n = int(input())
st = 20
for i in range(0,n):
    print(st,end=" ")
    st=st+40+(i*4)