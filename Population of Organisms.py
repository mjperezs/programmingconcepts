'''
Maria Jose Perez
U77568172
Description: The code calculates the size of a population of organisms by prompitng the user
to insert the number of organismss, average daily increase (%) and the number of days.

'''

numorg = int(input('Starting number of ogranisms: '))
while numorg < 1: 
    numorg = int(input('Starting number of ogranisms: '))
    while  numorg >= 1:
        break

increase = float(input('Average daily increase (as a %): '))
while increase < 1: 
    increase = float(input('Average daily increase (as a %): '))
    while  increase >= 1:
        break

numdays = int(input('Number of days to multiply: '))
while numdays < 1:
    numdays = int(input('Number of days to multiply: '))
    while  numdays >= 1:
        break

print('Day\t\t\tPopulation\n----------------------------------')


for i in range(numdays):
    print(f'{i+1}\t\t\t{numorg:.6f}')
    numorg = numorg + (numorg * increase/100)
