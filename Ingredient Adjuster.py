
#constants
cups_of_sugar = 1.5 
cup_of_better = 1
cups_of_flour = 2.75

num_of_cookies = float(input('Enter the number of cookies: '))
sugar = (1.5 / 48) * num_of_cookies
butter = (1 / 48) * num_of_cookies
flour = (2.75 / 48) * num_of_cookies
                       
print('To make', num_of_cookies, 'cookies, you will need: \n{:,.2f} cups of sugar \n{:,.2f} cups of butter \n{:,.2f} cups of flour'.format(sugar,butter,flour))
