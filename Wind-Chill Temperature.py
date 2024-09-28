'''María José Pérez U77568172
Description: In this code, I used the while loop to get the correct
temperature and speed range along with the arithmetic expressions and
format for decimal outputs. 
'''


temperature = float(input('Enter the temperature in Fahrenheit: '))

while temperature < -58 or temperature > 41:
    temperature = float(input('Temperature must be between -58F and 41F \nPlease re-enter the temperature in Fahrenheit: '))

speed = float(input('Enter the wind speed miles per hour: '))

while speed < 2:
  speed = float(input('Speed must be greater than or equal to 2 \nPlease re-enter the wind speed miles per hour:'))
    
wind_chill_temp = 35.74 + (0.6215 * temperature) - (35.75 * (speed**0.16)) + (0.4275 * temperature * (speed**0.16))
print((f'The wind chill index is {wind_chill_temp:.1f}'))




