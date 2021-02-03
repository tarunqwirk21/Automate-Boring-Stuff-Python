import random

print(' Hello, May i know your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 6')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good Job' + 'You guessed my number in' + guessesTaken + 'guesses')
else:
    print('No, the number i was thinking of is' + int(secretNumber))
