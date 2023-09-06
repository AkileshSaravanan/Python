'''
"Pine Tree" is a recently launched startup Event Management company. 
The company gained a good reputation within a short span because of its highly reliable service delivery. 
As per the new administrative policies of the company, the Chairman of the company is elected every 4 years, the Finance Director is appointed every 2 years, the Chief Technical Director is elected every 3 years and the Security Chief is replaced every 5 years.
This year, in Year X, the newly elected Chairman announced the appointment of the Finance Director, and a new Chief Technical Director, and congratulated the Security Chief for winning the recent election. 
That is, all positions were changed over. This is highly unusual. You will quantify how unusual this really is.

Write a program that inputs the year X and the future year Y and lists all years between X and Y inclusive of when all positions change.

Input format :
The first line of the input is an integer that corresponds to the year X.
The second line of the input is an integer that corresponds to the future year Y.

Output format :
The output prints the list of years between X and Y inclusive when all positions change.

Refer to the sample output for formatting specifications.

Sample test cases :
Input 1 :
2004
2100

Output 1 :
All positions change in year 2004
All positions change in year 2064

Input 2 :
1900
2017

Output 2 :
All positions change in year 1900
All positions change in year 1960
'''
y1 = int(input())
y2 = int(input())
while True:
    if y1<=y2:
        print("All positions change in year",y1)
    else:
        break
    y1=y1+60