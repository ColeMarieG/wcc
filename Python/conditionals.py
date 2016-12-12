
# # Tip calculator with three tip percentage options
# meal_price = float(raw_input('How much was your meal? '))
# print('How would you rate the service? ')
# print('a. Not so good')
# print('b. Good')
# print('c. Excellent!')
# chosen_option = raw_input('Choose an option: ')
#
# # Here's where conditionals come in...
# if chosen_option == 'a':
#     percentage = .15;
# elif chosen_option == 'b':
#     percentage = .18;
# else:
#     percentage = .20;
#
# tip = meal_price * percentage
# total_price = meal_price + tip
# print('You should tip $' + str(tip))
# print('Your total cost would be $' + str(total_price))


# # Input temp, output what you should wear
# temp = int(raw_input('What is the temperature?'))
#
# print('You should bring the following items:')
# if temp <= 40:
#     print('Heavy Coat')
#     print('Hat')
#     print('Gloves')
# elif temp <= 70:
#     print('Light Coat')
#     print('Hat')
# else:
#     print('Nothing!')


# #Determine is someone is baby/child/adult based on age
# age = int(raw_input('How old are you?'))
# if age < 3:
#     print('baby')
# elif age < 18:
#     print('child')
# else:
#     print('adult')


# #Determine is someone is baby/child/adolecent/adult based on age
# age = int(raw_input('How old are you?'))
# if age < 3:
#     print('baby')
# elif age < 16:
#     print('child')
# elif age < 18:
#     print('adolescent')
# elif age < 21:
#     print('young adult')
# else:
#     print('adult')


# # Either/or conditional (no elif)
# age = int(raw_input('How old are you?'))
# if age < 18:
#     print('child')
# else:
#     print('adult')


# # Non-chained conditional, more than one option can be temperature
# age = int(raw_input('How old are you?'))
# if age > 16:
#     print('You can drive')
# if age > 18:
#     print('You can vote')
# if age > 21:
#     print('You can join the military')
# if age > 75:
#     print('You can retire')


# Update of branched tip calculator
meal_price = float(raw_input('How much was your meal? '))
print('How would you rate the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
chosen_option = raw_input('Choose an option: ')

# Here's where conditionals come in...
if chosen_option == 'a':
    percentage = .15
elif chosen_option == 'b':
    percentage = .18
elif chosen_option == 'c':
    percentage = .20
else:
    percentage = .20
    print('You did not enter a valid option, defaulting to 20%')

tip = meal_price * percentage
total_price = meal_price + tip
print('You should tip $' + str(round(tip, 2)))
print('Your total cost would be $' + str(round(total_price, 2)))
