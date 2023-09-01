'''
The "Pine Tree" Event Management Company helps you plan and execute it better and faster, be it a last-minute get-together, a birthday party, or a corporate event. Nikhil, the founder of the company wanted the Pineaxe Event Management System to get and display the event details from his Customers for every new order of the Company.
Write a program that will get the input of the event details like the name of the event, type of the event, number of people expected, a string value (Y/N) telling whether the event is going to be a paid entry, and the projected expenses (in lakhs) for the event. The program should then display the input values as a formatted output.
Input format:
The first input is a string corresponding to the event's name. Assume the maximum length of the string as 50.
The second input is a string that corresponds to the type of event. Assume the maximum length of the string as 50,
The third input is an integer corresponding to the number of people expected for the event.
The fourth input is a character that corresponds to Y/N telling whether the event is going to be a paid entry or not.
The fifth input is a double value that corresponds to the projected expenses (in lakhs) for the event.
Output format:
The output should display the event details as given in the sample output. All double values need to be displayed correctly to I decimal place.
Refer to the sample output for formatting specifications.
Sample test cases:
Input 1:
Food Fest 2017
Public
5000
Y
5.7
Output 1:
Event Name: Food Fest 2017
Event Type: Public
Expected Count: 5000
Paid Entry: Y
Projected Expense: 5.7L
'''

# Input event details
event_name = input()
event_type = input()
expected_count = int(input())
paid_entry = input()
projected_expense = float(input())

# Display event details in the specified format
print("Event Name:", event_name)
print("Event Type:", event_type)
print("Expected Count:", expected_count)
print("Paid Entry:", paid_entry)
print("Projected Expense:", "{:.1f}L".format(projected_expense))
