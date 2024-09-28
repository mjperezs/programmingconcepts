'''
Maria Jose Perez
U77568172
DESCRIPTION: The code prompts the user to enter the sides and length of them,
Retail Items.py


'''

import math

class Polygon:
    def __init__(self, n=0,s=0.0):
        self.__sides = n
        self.__length = s

    def setSides(self,n):
        self.__sides = n
        
    def setLength(self,s):
        self.__length = s
        
    def getSides(self):
        return self.__sides
    
    def getLength(self):
        return self.__length

    def Perimeter(self):
        return self.__sides * self.__length

    def Area(self):
        a = (self.__sides * self.__length * self.__length)/(4 * math.tan(math.pi/self.__sides))
        return a

def main():
    poly = Polygon()
    
    sides = int(input('Enter the number of sides (>=3):'))
    
    while sides < 3:
        sides = int(input('Invalid entry. Re-enter the number of sides (>=3):'))

    length = float(input('Enter the length of each sides (>=0.1):'))
    
    while length < 0.1:
        length = float(input('Invalid entry. Re-enter the length of each sides (>=0.1):'))

    poly.setLength(length)
    
    poly.setSides(sides)
    
    print(f'The polygon has {poly.getSides()} sides. Each sides is {poly.getLength()} units in length.')

    print(f'The perimeter of the polygon is {poly.Perimeter():.3f} units and its area is {poly.Area():.3f} square units.')

main()
