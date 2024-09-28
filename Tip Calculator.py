'''
Enter the subtotal: $1250
Enter tip amount (as a %): 25
Subtotal: $ 1,250.00
Tip: $ 312.50
Total: $ 1,562.50
'''

subtotal = float(input('Enter the subtotal: $'))
tip = float(input('Enter tip amount (as a %): '))
tip_ = subtotal*(tip/100)
print('Subtotal: ${:,.2f}'.format(subtotal))
print('Tip: $', format(tip_,'.2f'))
total = subtotal + tip_
print('Total: ${:,.2f}'.format(total))
