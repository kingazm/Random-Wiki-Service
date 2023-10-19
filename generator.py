import requests
import webbrowser
from bs4 import BeautifulSoup #webscraping magic
import datetime #provides current time to file log
#import wikipedia #provides summaries, deactivated for now

#Stored text options for both language options
greeting = {
    "PL": "Dzien dobry! Jesli tutaj jestes, zapewne sie nudzisz...\n",
    "EN": "Hello! If you're here, that means you must be really bored...\n",
    }

whatchaSay = {
    "PL":"Co powiesz na ten losowo wybrany artykuł? Czytamy dalej?\n T/N",
    "EN": "How about this randomly choosen article? Wanna read more?\n Y/N",
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

#Core function generating the article from basic webscraping
def randomArticle():

    if lang == "EN":
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        urlOfLang = "https://en.wikipedia.org/wiki/%s"

    elif lang == "PL":
        url = requests.get("https://pl.wikipedia.org/wiki/Special:Random")
        urlOfLang = "https://pl.wikipedia.org/wiki/%s"

    soup = BeautifulSoup(url.content, "html.parser")
    articleTitle = soup.find(class_="firstHeading").text
    print(articleTitle)

    #checks if the answer is correct format, then goes to the website
    print(whatchaSay[lang])
    answer = input("").upper()

    if answer=="T" or answer=="Y":
        print(articleAdded[lang])
        
        file.write(str(datetime.datetime.now()))
        file.write("    ")

        url = urlOfLang % articleTitle
        webbrowser.open(url)

        ratingValidator()
                               
    elif answer=="N":
        print("\n")
        userService(lang)

    else:
        print(invalidAnswer[lang])
        answerValidator()

    #if lang == "EN":
        #articleSummary = wikipedia.summary(articleTitle)
        #print(articleSummary) #summary causes some issues in PL for now, too long in EN at times
        
    return articleTitle

#Making sure the rating given by user is within the given range
def ratingValidator():
    print(rate[lang])
    rating = input("")

    if int(rating)<=5 and int(rating) >=0:
        print("Super!")

    else:
        print(invalidRating[lang])
        ratingValidator()
            
#Making sure the answer given by the user makes sense (Y/N or T/N format)
def answerValidator():
    answer = input("").upper()

    if answer=="T" or answer=="Y":
        print(articleAdded[lang])
        
        file.write(str(datetime.datetime.now()))
        file.write("    ")

        url = "https://en.wikipedia.org/wiki/%s" % articleTitle
        webbrowser.open(url)

        ratingValidator()
                               
    elif answer=="N":
        print("\n")
        userService(lang)

    else:
        print(invalidAnswer[lang])
        answerValidator()
    
#A function tying the whole program together, containing all the other functions
def userService(lang):
    randomArticle()
    #print(whatchaSay[lang])
    #answerValidator()
    
    file.close()


#Here goes the Service!
print("Your cure for curiosity and boredom")
print("Randomized Wikipedia article")

lang = ""

#Language choosing section for best experience
while lang != "PL" and lang != "EN":
    print("Choose language:\n")
    print("PL / EN")
    lang = input("").upper()
    
print(greeting[lang])
userService(lang)

input("Hit enter to exit")
exit()
        


