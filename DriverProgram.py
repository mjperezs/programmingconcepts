'''
Maria Jose Perez
U77568172
DESRIPTION: This module prompts the user to enter a guess for the questions asked
while it counts how many points were earned by each player and
displays a winner.

'''

from TriviaQuestions import get_question

scores = [0, 0]

playerturn = 0

question = get_question()

for q in question:
    if playerturn == 0:
        print('Question for the first player:')
    else:
        print('Question for the second player:')

    print(str(q))

    guess = int(input('Enter your solution (a number between 1 and 4): '))

    if guess == q.numcorrect:
        print('This is the correct answer. \n')
        scores[turn] += 1
    else:
        print(f'That is incorrect. The correct answer is {q.numcorrect}. \n')

    if playerturn == 1:
        playerturn = 0
    else: 
        playerturn = 1

if scores[0] > scores[1]:
    winner = 'first'
else:
    winner = 'second'

print(f'The first player earned {scores[0]} points.')
print(f'The first player earned {scores[1]} points.')
print(f'The {winner} player wins the game.')





