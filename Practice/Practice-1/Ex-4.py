'''
Total Expenses for the Event
The prime functionality of an Event Management System is budgeting.An Event Management System should estimate the total expenses incurred by an event and the percentage rate of each of the expenses involved in planning and executing an event. 
Nikhil, the founder of "Pine Tree" wanted to include this functionality in his company’s Pineaxe Event Management System and requested your help in writing a program for the same. 
The program should get the branding expenses, travel expenses, food expenses, and logistics expenses as input from the user and calculate the total expenses for an event and the percentage rate of each of these expenses.

Input format :
The first input is a double value that corresponds to the branding expenses.
The second input is a double value that corresponds to the travel expenses.
The third input is a double value that corresponds to the food expenses.
The fourth input is a double value that corresponds to the logistics expenses.

Output format :
The first line of the output should display the double value that corresponds to the total expenses for the Event.
The next four lines should display the percentage rate of each of the expenses.

Refer to the sample output for formatting specifications.
Sample test cases :
Input 1 :
20000
40000
15000
25000
Output 1 :
100000.00
20.00%
40.00%
15.00%
25.00%
'''

brexp = float(input())
trexp = float(input())
foexp = float(input())
loexp = float(input())
t = round(float(brexp+trexp+foexp+loexp),2)
print("{:.2f}".format(t),end="")
print("\n{:.2f}".format(brexp*100/t),end="%")
print("\n{:.2f}".format(trexp*100/t),end="%")
print("\n{:.2f}".format(foexp*100/t),end="%")
print("\n{:.2f}".format(loexp*100/t),end="%")