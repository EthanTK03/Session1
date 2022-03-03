import random

age = input('What is your age? ')

correct = 0 #for keeping track of correct answers
question = 0
for q in range(1,11): #amount of loops
    print('Problem ' + str(q))
    x = random.randrange(1,10) #random number between 1 and 9
    y = random.randrange(1,10) #same as x
    ans = input('what is ' + str(x) + '+' + str(y) + '? ') #first number + second number
    ans = int(ans) #turns into number
    if ans == x+y: #check if correct, show below if correct
        print('Well done')
        correct = correct + 1 #keep track of correct answers
    else: #if wrong, show below
        print('wrong, ', x, '+', y, '=', correct)

print("You got " + str(correct) + " correct. Good effort!")