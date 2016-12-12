# answer1_correct = True
# answer2_correct = False
#
# print(1 == 1) # Expected output: True


# ==	Equal
# !=	Does not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal
# <=	Less than or equal


# print(1 == 2) # Expected output: False
# print(1 > 2) # Expected output: False
# print(2 > 1) # Expected output: True
# print(1 >= 1) # Expected output: True
# print(2 == 2) # Expected output: True
# print(2 != 2) # Expected output: False


# age = 30
# print(age > 10) # Expected outcome: True
# print(10 < age) # Expected outcome: True
# print(age > 10 + 20) # Expected outcome: False
# print(age + 20 > 10) # Expected outcome: True

# # When comparing strings assign #to letters like a=1 z=26, then compare
# print('a' > 'z') # Expected outcome: F
# print('z' > 'a') # Expected outcome: T
# print('apples' > 'oranges') # Expected outcome: F
# print('oranges' > 'apples') # Expected outcome: T
# print('cat' > 'car') # Expected outcome: T
# print('car' > 'cat') # Expected outcome: F

# # Be careful not to compare strings and ints or floats
# answer = raw_input('What is 1 + 1? ')
# print(answer == 2)
# # This is better
# answer = int(raw_input('What is 1 + 1? '))
# print(answer == 2)

# age = 1
# print(age > 12 and age < 19) # Expected outcome: False
# age = 14
# print(age > 12 and age < 19) # Expected outcome: True
# age = 19
# print(age > 12 and age < 19) # Expected outcome: False
# age = 18
# print(age > 12 and age < 19 and age != 5) # Expected outcome: True
# age = 5
# print(age > 12 and age < 19 and age != 5) # Expected outcome: False
# age = -1
# print(age > 12 and age < 19) # Expected outcome: False
# age = 10
# print(age > 25 and age < 15) # Expected outcome: False
# # Could the above expression ever be True? NO

# gesture = 'rock'
# print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: True
# gesture = 'pape'
# print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: False

age = int(raw_input('How old are you?'))
print(age >= 5 and age <= 10)
print (not age <5 and not age > 10)
