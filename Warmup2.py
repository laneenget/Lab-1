'''
Lane Enget | ITEC 2905 | 1/15/2020
This program adds input classes to a list and prints them.
'''

num_classes = int(input('How many classes are you taking this semester? ')) #instantiate number of classes

classes = [] #create empty class list

i = 0
while i < num_classes: #use a while loop to add user input to list
    course = input('Enter the name of the class: ') #add class name to variable
    classes.append(course) #add class to list
    i += 1

print("The classes you are taking are: ")

for x in classes: #print classes
    print(x)