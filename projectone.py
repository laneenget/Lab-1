'''
Lane Enget | ITEC 2905 | 1/16/2020
This program simulates the game of MASH. MASH is a paper and pen game where
you fill in options for certain categories, generate a random number, and
eliminate choices until only one option for each category remains. Your life
is predicted with these options.
'''

import random

def main():
    try:
        spouses, careers, cities, kids = inputs()
        house, spouse, career, city, kid = processing(spouses, careers, cities, kids)
        outputs(house, spouse, career, city, kid)
    except Exception as err:
        print(err)

def inputs():
    print('Welcome to the game of MASH!')
    n = 4 #instantiate number of entries
    spouses = [] #create empty lists for spouses, careers, cities, and kids
    careers = []
    cities = []
    kids = []

    print('Enter four potential spouses: ')
    for i in range(0, n): #Enter the appropriate number of spouses for n
        spouse = input()
        while spouse == '': #Validate user input
            spouse = input('Please enter a name: ')
        spouses.append(spouse) #Add each spouse to list
    
    print('Enter four potential careers: ')
    for i in range(0, n): #Enter the appropriate number of careers for n
        career = input()
        while career == '': #Validate user input
            career = input('Please enter a career: ')
        careers.append(career) #Add each career to list

    print('Enter four cities: ')
    for i in range(0, n): #Enter appropriate number of cities for n
        city = input()
        while city == '': #Validate user input
            city = input('Please enter a city: ')
        cities.append(city) #Add each city to list

    print('Enter four numbers: ')
    for i in range(0, n): #Enter appropriate number of numbers for n
        number = input()
        while number.isnumeric() is False or int(number) < 0: #Validate nonnegative numeric entry
            number = input('Please enter a whole number: ')
        number = int(number) #Turn number to integer
        kids.append(number) #Add number to list

    return spouses, careers, cities, kids

def processing(spouses, careers, cities, kids):
    houses = ['mansion', 'apartment', 'shack', 'house'] #Create houses list
    
    #Generate a random number for each category and pick the appropriate index value in each list
    n = random.randint(0, len(houses) - 1)
    house = houses[n] #Instantiate randomized house
    n = random.randint(0, len(spouses) - 1)
    spouse = spouses[n] #Instantiate randomized spouse
    n = random.randint(0, len(careers) - 1)
    career = careers[n] #Instantiate randomized career
    n = random.randint(0, len(cities) - 1)
    city = cities[n] #Instantiate randomized city
    n = random.randint(0, len(kids) - 1)
    number = kids[n] #Instantiate random number of kids

    return house, spouse, career, city, number

#Print output in a readable way    
def outputs(house, spouse, career, city, number):
    print('MASH is a predictor of your future life. Based on your entries, here is what you can expect: ')
    print('You will live in a ' + house + ' in ' + city + '.')
    print('You will marry ' + spouse + '.')
    print('Together, you will have ' + str(number) + ' kids.')
    print('You will make your living as a ' + career + '.')
    print('You will live a happy life.')

main()