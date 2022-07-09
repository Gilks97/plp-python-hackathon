#Bus fare challenge
from datetime import date
today = date.today()
day = today.strftime('%A')[:3]
print("Date:", today)
print("Day:", day)
week = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
if week[day] in range(0, 5):
    fare = 100
elif week[day] == 5:
    fare = 60
else:
    fare = 80
print("Fare:", fare)

#Sales tax challenge
print('*****Painting Company*****')
wall_area = int(input('enter the square feet of wall to be painted: '))
price = int(input('enter the price price of paint/gallon: '))
paint_gallons = int(input('enter no. of gallons of paint required: '))
hours = (wall_area*8)/115
labor_cost = 20*hours
total_cost = labor_cost + price
print(f'Number of gallons of paint required: {paint_gallons}')
print(f'Square feet of wall to be painted: {wall_area}')
print(f'Hours of labor required: {hours}')
print(f'cost of the paint: {price}')
print(f'labour charges: {labor_cost}')
print(f'Total cost of the paint job: {total_cost}')


#Personality test program
print('****Welcome to Book Club*****')
books = int(input('enter number of books purchased this month: '))
if books == 0:
    print('points awarded: 0' )
elif books == 1:
    print('points awarded: 6')
elif books == 2:
    print('points awarded: 16')
elif books == 3:
    print('points awarded: 32')
else:
    print('points awarded: 60')

#Door lock system challenge
import datetime
now = datetime.datetime.now()
password = 'jkl'
pswd = input('enter password: ')
while pswd != password:
    print('Ooops!! error')
    pswd = input('enter password: ')
else:
    command = ''
    opened = False
    closed = False
    while command != 'quit':
        command = input('>').lower()
        if command == 'open':
            if opened:
                print('The door is already open!!')
            else:
                opened = True
                print('The door is now open')
                print("Door last open at : ")
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
        elif command == 'close':
            if closed:
                print('The door is already locked')
            else:
                closed = True
                print('The door is now locked')
                print("Door last closed at : ")
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
        elif command == 'quit':
            print('Process terminated')
        else:
            print('Invalid input')


#Day 3 calories challenge
number_of_fat_grams = int(input('Grams of fat consumed: '))
number_of_carb_grams = int(input('Grams of carbs consumed: '))
calories_from_fat = number_of_fat_grams*9
calories_from_carb = number_of_carb_grams*4
total_calories = calories_from_fat + calories_from_carb
print('calories from fat: ', calories_from_fat)
print('calories from carbs: ', calories_from_carb)
print('You consumed', total_calories, 'calories')

