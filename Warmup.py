'''
Lane Enget | ITEC 2905 | 1/15/2020
This program asks for user name and birth month
'''
name = input('What is your name? ') #take name input
month = input('What month were you born in? ') #take month input

print('Hello ' + name) #print name

if month == 'January':
    print('Happy birthday month') #print happy birthday if input month is January

print('There are ' + str(len(name)) + ' letters in your name') #print letter count in name input