first_d = input('Enter the first diagonal length: ')
second_d = input('Enter the second diagonal length: ')
radius = input('Enter the radius of the enclosed circle: ')
kite = (float(first_d)*float(second_d))/2
import math
circle = float(math.pi)*(float(radius)**2)


area = float(kite) - float(circle)
print('The shaded area is',format(area,'.3f'),'square units.')
