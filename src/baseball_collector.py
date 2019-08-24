'''
- First import the sqlite and beautiful soup (web scrapping) libraries
- Create a function to collect the information from baseball reference using beautiful soup
- Then create an sql database and create tables based on player's name alphabetically
- add height/weight to the database to be able to filter and organize on the webapp
'''

import sqlite3
import requests
import logging
from bs4 import BeautifulSoup
def scrape_data_website():
    start_url = 'https://www.baseball-reference.com/players/a'
    base_url = 'https://www.baseball-reference.com'
    response = requests.get(start_url)
    
    soup_handler = BeautifulSoup(response.text, "html.parser")
    temp = soup_handler.find_all('b') # bold means the player are active

    urls = []
    for i in temp:
        if i.a == None:
            continue
        
        urls.append(base_url + i.a.get('href'))
        
    
    print(urls)



if __name__ == '__main__':
    scrape_data_website()