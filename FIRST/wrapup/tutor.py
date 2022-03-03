import random

age = input('What is your age?')

correct = 0 #for keeping track of correct answers
question = 0
for q in range(1,11):
    x = random.randrange(1,10)
    y = random.randrange(1,10)
    ans = input('what is ' + str(x) + '+' + str(y) + '? ')
    ans = int(ans)
    if ans == x+y:
        print('Well done')
        correct = correct + 1 #keep track of correct answers
    else:
        print('wrong, ', x, '+', y, '=', correct)

print("You got " + str(correct) + " correct. Good effort!")