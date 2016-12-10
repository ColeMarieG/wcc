# name = raw_input('What is your name? ')
# print('Hi ' + name)


# name = raw_input('What is your name?')
# age = raw_input('How old are you?')
# print(name + ' is ' + age + ' years old.')

# # raw_input value is always a string
# age = raw_input('How old are you?')
# dog_years = int(age) * 7
# print('You are ' + str(dog_years) + ' years old in dog years.')


# Create a tip calculator
meal_cost = float(raw_input('How much was your meal? '))
tip = meal_cost * .2
total_cost  = tip + meal_cost
print('You should tip $' + str(round(tip, 2)))
print('Your total is $' + str(round(total_cost, 2)))
