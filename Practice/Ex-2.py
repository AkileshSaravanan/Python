'''
Kabali is a brave warrior who with his group of young ninjas moves from one place to another to fight against his opponents. Before Fighting he just calculates one thing, the difference between his ninja number and the opponent's ninja number. From this difference, he decides whether to fight or not. Kabali's ninja number is never greater than his opponent's. The input contains two numbers in every line. These two numbers in each line denote the number of ninjas in Kabali's clan and his opponent's clan. print the difference in the number of ninjas between Kabali's clan and his opponent's clan. Each output should be in a separate line.
Input format:
The first line of input contains an integer representing the number of ninjas in Kabali's team
The second line of input contains an integer representing the number of ninjas in the opponent's team
Output format:
The output displays the difference between two input values.
Sample test cases:
Input 1:
200
100
Output 1:
100
Input 2:
100
200
Output 2:
100
'''
# Input the number of ninjas in Kabali's team and the opponent's team
kabali_ninjas = int(input())
opponent_ninjas = int(input())

# Calculate the difference between the two teams' ninja numbers
if(kabali_ninjas>opponent_ninjas):
    difference = kabali_ninjas - opponent_ninjas
    print(difference)
if(opponent_ninjas>kabali_ninjas):
    difference = opponent_ninjas - kabali_ninjas 
    print(difference)
