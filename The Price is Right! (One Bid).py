'''Mariía José Pérez U77568172

Description: For this code, I imported the random module so the prize price could be a random number (randit helped me to obtain an integer value).
Then, used append to put the prices in a list, so later I can index them and compare which one is closer to the prize price.
Also, used if and elif to evaluate the different situations with the values entered in case some where the exact bid, overbid, or underbid. 

'''

import random

prize_price = random.randint(1000,5000)
prices = []
player1 = int(input('Player 1, what is your bid? '))
player2 = int(input('Player 2, what is your bid? '))
player3 = int(input('Player 3, what is your bid? '))
player4 = int(input('Player 4, what is your bid? '))

if player1 == prize_price:
    print(f'Ding Ding Ding! One player got it exactly right and gets $500! \nActual price is ${prize_price}! Player 1, come on up!')
elif player2 == prize_price:
    print(f'Ding Ding Ding! One player got it exactly right and gets $500! \nActual price is ${prize_price}! Player 2, come on up!')
elif player3 == prize_price:
    print(f'Ding Ding Ding! One player got it exactly right and gets $500! \nActual price is ${prize_price}! Player 3, come on up!')
elif player4 == prize_price:
  print(f'Ding Ding Ding! One player got it exactly right and gets $500! \nActual price is ${prize_price}! Player 4, come on up!')


player1 = prize_price -player1
player2 = prize_price -player2
player3 = prize_price -player3
player4 = prize_price -player4

prices.append(player1)
prices.append(player2)
prices.append(player3)
prices.append(player4)


y = prize_price
for i in prices:
  x = i
  
  if x < y and x > 0:
    y = x

if y == player1:
  print(f'Actual price is ${prize_price}! Player 1, come on up!')
elif y == player2:
  print(f'Actual price is ${prize_price}! Player 2, come on up!')
elif y == player3:
  print(f'Actual price is ${prize_price}! Player 3, come on up!')
if y == player4:
  print(f'Actual price is ${prize_price}! Player 4, come on up!')         

    
    
