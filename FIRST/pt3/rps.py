import random

#1 - rock
#2 - paper
#3 - scissors

comp = random.randrange(1,4)

user = input('choose 1 for rock, 2 for paper, 3 for scissors: ')
user = int(user)

if user < 1 or user > 3:
    print("that's not how you play rock-paper-scissors. Leave.")
else:
    print("You choose: ", user)
    print("I choose: ", comp)

if user == 1: #rock
    if comp == 1:
        print('TIE')
    if comp == 2:
        print('COMPUTER FOR THE WIN')
    if comp == 3:
        print('You cheatin I swear. user wins')
    
if user == 2: #paper
    if comp == 1:
        print('ow. You win')
    if comp == 2:
        print('tie...')
    if comp == 3:
        print('LETS GO, COMP WINS')

if user == 3: #scissors
    if comp == 1:
        print('I. WIN. ')
    if comp == 2:
        print('tis a tie, shall we go again?')
    if comp == 3:
        print('user wins... CONGRATULATIONS')