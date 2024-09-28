'''
Maria Jose Perez
U77568172
DESRIPTION: This code stores the questions that are going to be asked to both players.

'''
from QuestionsClass import TriviaQuestion

def get_question():
    question = []
    question.append(TriviaQuestion("Who is the main character in the TV Show 'Dynasty'?",'Blake Carrington','Fallon Carringotn','Michael Culhane','Sammy Joe','2'))
    question.append(TriviaQuestion("Who is Fallon's husband in the TV show 'Dynasty'?",'Jeff Colby','Liam Ridley','Adam Carrington','Michael Culhane','2'))
    question.append(TriviaQuestion("What is name of the house of the Carrington's",'Carrington Manor','Carrington Mansion','Carrington House','Carrington Penthouse','1'))
    question.append(TriviaQuestion("Who is not Blake Carrington's son in the TV Show 'Dynasty'?",'Adam','Fallon','Steven','Amanda','3'))
    question.append(TriviaQuestion("Which was Michael Culhane's job at the Carrington Manor?",'bodyguard','chef','butler','chauffeur','4'))
    question.append(TriviaQuestion("What is the name of Fallon and Liam's daughter in the TV Show 'Dynasty'?",'Fallon','Lauren','Laura','Alexis','2'))
    question.append(TriviaQuestion("Who is the daughter of Anders in the TV Show 'Dynasty'?",'Amanda','Kirby','Fallon','Cristal','2'))
    question.append(TriviaQuestion('Which is the middle name of Fallon Carrigton','Alexis','Lauren','Morell','Anastacia','3'))
    question.append(TriviaQuestion("What is the name of the dog of the Carringtons in the TV Show 'Dynasty?",'Bob','Tom','Max','Bo','4'))
    question.append(TriviaQuestion("Which one is the oldest of the Carrington's siblings?",'Fallon','Steven','Amanda','Adam','4'))
    
    return question 
