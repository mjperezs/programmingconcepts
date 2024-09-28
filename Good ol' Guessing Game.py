'''
Maria Jose Perez
U77568172
Description: the code assigns a random number to the right guess and prompts the user with 10
tries to guess the right number. If the guess is higher, it will get back with 'too high! or if it
is lower; with 'too low'. If guesssed it will congratulate you and let you know how many guess you took.
After 10 failed tries, it will give you the right guess.

'''
import random
right = random.randint(1,101)

number = float(input('Enter a number between 1 and 100 (inlcusive): '))

tries = 0
while tries <= 9:
    if number < right:
        number = int(input('Too low. Enter another guess: '))
    if number > right:
        number = int(input('Too high. Enter another guess: '))
    if number == right:
        break
    tries += 1
tries = tries

if number == right:
    print(f'You guessed it right! You got in {tries} guesses!')
    

if number != right:
    right = str(right)
    print(f'Sorry, the number was {right}')


