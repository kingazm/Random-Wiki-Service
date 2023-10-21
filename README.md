# Random-Wiki-Service - what is that?

Have you ever needed something new to read in your spare time, not to procrastinate or endlessly scroll but you've run out of ideas, articles, books?

Here's your sollution, presenting Random Wiki Service - an app providing user-friendly experience - random Wikipedia articles in English and Polish.

After choosing the language, the app proposes new articles until the user is satisfied. Then, opens said article directly in the browser and saves the current date, link/title and article's rating given by user, maintaining this log of fun information for later.

Disclaimer: may require additionally installing requests and Beautiful Soup 4, so commands:

pip install requests (pip3 on MacOS)
pip install BeautifulSoup4

# Tech stack

Python, BeautifulSoup library (webscraping), (other libraries will be listed soon!)


# How to use it?

Important note: to run the app, you must have Python installed.
To do that first, go to the link below and follow the instrutions on the official Python website:
https://www.python.org/downloads/

1. Having python on your computer, download the files from GitHub (.zip)
(The text file will be created on your computer locally if it does not already exist, the key one is generator.py).

2. Then you need to have Beautiful Soup and Requests libraries installed. <br> To do that, open Command Line and type: <br>
pip install beautifulsoup4 (pip3 on MacOS)
pip install requests

3. To run .py program, open Command Line in the directory of the folder you've saved the generator.py or manually go to that path using <br> cd (here goes folder you want to enter) <br>
This may take a couple of commands, depending on where exactly is the file.

You can check if you've entered the right folder by using<br>
ls<br>
which lists all the elements in the directory.

After entering the folder with generator.py, type<br>
python generator.py (or python3 generator.py on MacOS)

And voila! The app is running in the Command Line!
