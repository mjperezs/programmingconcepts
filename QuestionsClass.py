'''
Maria Jose Perez
U77568172
DESRIPTION: This module includes the class that will be used further in the other modules and
includes the __init__ and __str__ method that store parameters for the entire code. 

'''

class TriviaQuestion:
    def __init__(self,question,answ1,answ2,answ3,answ4,numcorrect):
        self.question = question
        self.answ1 = answ1
        self.answ2 = answ2
        self.answ3 = answ3
        self.answ4 = answ4
        self.numcorrect = numcorrect

    def __str__(self):
        print_str = ''
        print_str += self.question + '\n'
        print_str += '1. ' + self.answ1 + '\n'
        print_str += '2. ' + self.answ2 + '\n'
        print_str += '3. ' + self.answ3 + '\n'
        print_str += '4. ' + self.answ4

        return print_str
    
    
