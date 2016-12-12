import random
#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
random.shuffle(cards)


# Round 1
print ('')
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))


# Round 2
print ('')
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

# Player's 2nd card based on hit or stay decision
if decision == "h":
    player_card2 = cards.pop()
else:
    player_card2 = 0

# Computer's 2nd card (computer always hits in round 2)
computer_card2 = cards.pop()

# hands after round 2
print('Player cards: ' + str(player_card1) + ', ' + str(player_card2))
print('Computer cards:  ' + str(computer_card1) + ', ' + str(computer_card2))


# Round 3
print ('')
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

# Player's 3nd card based on hit or stay decision
if decision == "h":
    player_card3 = cards.pop()
else:
    player_card3 = 0

# Computer's 3rd card (stay if current card sum is higher than 15)
if computer_card1 + computer_card2 < 16:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

# Hands after round 3
print('Player cards: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
print('Computer cards:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))


# Results
print('\nGame over...')
player_score = player_card1 + player_card2 + player_card3
computer_score = computer_card1 + computer_card2 + computer_card3

# # For testing score scenarios
# player_score = 18
# computer_score = 19 # Computer wins. (It was closest to 21.)
# player_score = 19
# computer_score = 18 # You win! (You were closest to 21.)
# player_score = 15
# computer_score = 15 #No one wins. (You and the computer tied.)
# player_score = 23
# computer_score = 6 # Computer wins. (You busted.)
# player_score = 23
# computer_score = 24 # No one wins. (You and the computer busted.)

# Score scenarios
if player_score > computer_score and player_score <= 21:
    print('You win! (You were closest to 21.)')
elif player_score == computer_score and computer_score <= 21:
    print('No one wins. (You and the computer tied.)')
elif player_score > 21 and computer_score > 21:
    print('No one wins. (You and the computer busted.)')
elif player_score > 21 and computer_score <= 21:
    print('Computer wins. (You busted.)')
else:
    print('Computer wins. (It was closest to 21.)')
