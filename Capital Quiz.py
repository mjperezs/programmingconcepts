'''
Maria Jose Perez
U77568172
DESCRIPTION: The code asks the user to enter the correct capital of the state.
If the user press 'q', then it tells you how many times you had it incorrect
and correct.

'''
import random
#A dictionary to store the states and their capitals as key value pairs

state_capitals = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas' : 'Little Rock' ,
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Gerogia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trento',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne'
}

#A random number generator to randomize the states referenced
#You may think it would be useful to retrieve the index of the dictionary to help with randomizing the questions.
#You can overcome this by converting the dictionary to a list using list() so you can retrieve indices.

stateList = list(state_capitals.keys())


correct = 0
incorrect = 0


#A while loop to stop the game. The program should indicate what the sentinel is so that the user can stop the game at any time.
#The while loop should include an if elif structure to keep track of the user’s correct and incorrect answers

guess = 0
while guess != 'q':
    
    state = random.choice(stateList)

    capital = state_capitals[state]
    
    guess = input(f'What is the capital of {state}? (or enter q to quit):')
    
    if guess == 'q':
        break
    elif guess.title() == capital:
        correct += 1
        print('That is correct')    
    elif guess.title() != capital:
        incorrect += 1
        print('That is incorrect')
    

print(f'You had {correct} correct responses and {incorrect} incorrect responses.')
        


    




























