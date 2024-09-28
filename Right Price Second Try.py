

import random

#prize_price = random.randint(1000,5000)

prize_price = int(200)

player1 = int(input('Player 1, what is your bid? '))
player2 = int(input('Player 2, what is your bid? '))
player3 = int(input('Player 3, what is your bid? '))
player4 = int(input('Player 4, what is your bid? '))

if player1 > prize_price and player2 > prize_price and player3 > prize_price and player4 > prize_price:
    print('Buzz! Aww... everyone has overbid!')
    
if player1 == prize_price or player2 == prize_price or player3 == prize_price or player4 == prize_price:
    print('Ding Ding Ding! One player got it exactly right and gets $500!')

if player1 < prize_price or player2 < prize_price or player3 < prize_price or player4 < prize_price:
    diff1 = abs(prize_price - player1)
    diff2 = abs(prize_price - player2)
    diff3 = abs(prize_price - player3)
    diff4 = abs(prize_price - player4)
    diff = [diff1, diff2, diff3, diff4]
    winner = min(diff)
    if player1 == winner:
        print(f'Actual price is ${prize_price}! Player 1 , come on up!')
    if player2 == winner:
        print(f'Actual price is ${prize_price}! Player 2 , come on up!')
    if player3 == winner:
        print(f'Actual price is ${prize_price}! Player 3 , come on up!')
    if player4 == winner:
        print(f'Actual price is ${prize_price}! Player 4 , come on up!')


'''
if player1 <= prize_price:
    if diff1 < abs(diff2) or diff1 < abs(diff3) or diff1 < abs(diff4):
        print(f'Actual price is ${prize_price}! Player 1, come on up!')
if player2 <= prize_price:
    if diff2 < abs(diff1) or diff2 < abs(diff3) or diff2 < abs(diff4):
        print(f'Actual price is ${prize_price}! Player 2, come on up!')
if player3 <= prize_price:
    if diff3 < abs(diff2) or diff3 < abs(diff1) or diff3 < abs(diff4):
        print(f'Actual price is ${prize_price}! Player 3, come on up!')
if player4 <= prize_price:
    if diff4 < abs(diff2) or diff4 < abs(diff3) or diff4 < abs(diff1):
        print(f'Actual price is ${prize_price}! Player 4, come on up!')
'''
