import random
#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# print(cards) # To see the list before being shuffled

random.shuffle(cards)

print(cards) # To see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

print(cards) # To see the list after two cards have been popped off.

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
