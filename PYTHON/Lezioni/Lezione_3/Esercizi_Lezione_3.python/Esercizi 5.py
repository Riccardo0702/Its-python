#5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'maserati'? I predict False.")
print(car == 'maserati')

car == "yellow"
print("Is car == 'yellow'? I predict True.")
print(car == 'yellow')

car == "fast" 
print("Is car == 'fast'? I predict True.")
print(car == 'fast')

#5-3
alien_color = 'grey'

if alien_color == 'grey':
    print("You just earned 5 points!")

if alien_color == 'purple':
    print("You just earned 5 points!")

#5-4
if alien_color == 'grey':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points for shooting the alien!")

#5-5
if alien_color == 'grey':
    print("You just earned 5 points!")
elif alien_color == 'purple':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")



#5-6

age:int = int(input('My age is:'))
if age < 2:
    print('Newborn')
elif age >= 2 and age < 4:
    print('Toddler')
elif age >= 4 and age < 13:
    print('kid')
elif age >= 13 and age < 20:
    print('Teenager')
elif age >= 20 and age < 65:
    print('Adult')
elif age >= 65:
    print('Elder')


#5-7

favorite_fruits:list = ['Apples','Kiwis', 'Oranges']
if 'Apples' in favorite_fruits:
    print('You like apples a lot')
elif 'Bananas' in favorite_fruits:
    print('You like bananas a lot')
elif 'Oranges' in favorite_fruits:
    print('You like Oranges a lot')

#5-8

usernames:list = ['Frank', 'Josie', 'Luke', 'Mark', 'admin']

for people in usernames:
    if people == 'admin':
        print(f'Hello admin, would you like to see a status report?')
    elif len(usernames) == 0:
        print('We need more people')     
#5-9
    else:
        print(f'Hello {people}, thank you for logging in!')

#5-10

current_users:list = ['John', 'Maria', 'Sam', 'Vincent', 'Caine']
new_users:list = ['Maria', 'Mark', 'Phenelophe', 'Mattew', 'JOHN']
users_old:list = list(map(str.upper, current_users))
for user in new_users:
    if user in users_old:
        print(f'The name {user} has already been taken')
    elif user != users_old:
        print(f'The name {user} is available')

#5-11

number_list:list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in number_list:
    if numbers == 1:
        print(f'{numbers}st')
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f'{numbers}rd')
    else:
        print(f'{numbers}th')
