'''
Maria Jose Perez
U77568172
Description: The program will prompt the user so the length and number of sides are prompted.
Then, the angle will be calculated, so the polygon can be drawn with the turtle module.


'''
import turtle

num_sides = int(input('Enter the number of sides between 3 and 12 (inclusive): '))
while  num_sides < 3 or num_sides > 12: 
    num_sides = int(input('Invalid number of sides. Enter a number between 3 and 12 (inclusive): '))
    while  3 <= num_sides <= 12:
        break

length = int(input('Enter the length of each side (> 50): '))
while  length < 50: 
    length = int(input('Please enter a larger length of each side:  '))
    while  length > 50:
        break

angle = int((180)*(num_sides - 2)/num_sides)
angle2 = int(180 - angle)

turtle.shape('turtle')
turtle.speed(7)


if num_sides == 5:
    polygon = 'pentagon'
elif num_sides == 6:
    polygon = 'hexagon'
elif num_sides == 7:
    polygon = 'heptagon'
    
for x in range(num_sides):
    turtle.forward(length)
    turtle.right(angle2)


turtle.write(f'{polygon}',font=('Arial', 20, 'normal'))
