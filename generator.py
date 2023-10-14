#import requests
#import webbrowser
#from bs4 import BeautifulSoup

import datetime

print("Your cure for boredom")
print("Randomized Wikipedia article")

#Language choosing section for best experience
print("Choose language:\n")
print("PL / EN")
lang = input("").upper()

greeting = {
    "PL": "Dzien dobry! Jesli tutaj jestes, zapewne sie nudzisz...\n",
    "EN": "Hello! If you're here, that means you must be really bored...\n",
    }

whatchaSay = {
    "PL":"Co powiesz na ten losowo wybrany artykuł?\n T/N",
    "EN": "How about this randomly choosen article?\n Y/N",
    }

articleAdded = {
    "PL": "Wysmienicie! Artykul został dodany do twojej listy.\n Znajdziesz ją w pliku MyRandomWikis.txt",
    "EN": "Awesome! Article was added to your list.\n You'll find it in MyRandomWikis.txt file"
    }

rate = {
    "PL": "Po przeczytaniu oceń artykuł w skali 0-5\n Moja ocena: ",
    "EN": "After reading make sure to rate the content on 0-5 scale\n My rating: "
    }

invalidRating = {
    "PL": "Coś poszło nie tak, oceń ponownie: ",
    "EN": "Something went wrong, try rating again: ",
    }

invalidAnswer = {
    "PL": "Coś poszło nie tak, odpowiedz ponownie: ",
    "EN": "Something went wrong, answer again: ",
    }

readMore = {
    "PL": "Czytamy dalej? T/N",
    "ENG": "Wanna read some more?",

    }


file = open("MyRandomWikis.txt", "a")


#print("Chosen language: " + languages[lang])

def randomArticle():
    article = "hehe"
    return article

def ratingValidator():
    print(rate[lang])
    rating = input("")


    if int(rating)<=5 and int(rating) >=0:
        file.write(randomArticle() + "    " + rating + "\n")
       


    else:
        
        print(invalidRating[lang])
        ratingValidator()

    print(readMore[lang])
    wannaReadMore = input("").upper

    if wannaReadMore=="T" or wannaReadMore=="Y":
        userService(lang)

    elif wannaReadMore=="N":
        quit()

        #else:
            #print(invalidAnswer[lang])

        #add invalid case when rating is a letter, cause error
        #fix the loop - after wanna read more uder service does not work the second time
            
    

def answerValidator():
    answer = input("").upper()

    if answer=="T" or answer=="Y":
        print(articleAdded[lang])

        
        

        file.write(str(datetime.datetime.now()))
        file.write("    ")

        ratingValidator()
            
            

        
                    
    elif answer=="N":
        print("\n")
        userService(lang)

    else:
        print(invalidAnswer[lang])
        answerValidator()
    

def userService(lang):

    print(randomArticle())
    print(whatchaSay[lang])

    answerValidator()


  
        
print(greeting[lang])


userService(lang)

file.close()
