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

    # urls = []
    # for i in temp:
    #     if i.a == None:
    #         continue
        
    #     urls.append(base_url + i.a.get('href'))
        
    
    temp_url = 'https://www.baseball-reference.com/players/a/abadfe01.shtml'
    response = requests.get(temp_url)
    soup_handler = BeautifulSoup(response.text, 'html.parser')

    # determine a way to go through each row to extract the data
    temp = soup_handler.find(id='')
    counter = 0
    arr = []
    for i in temp:
        print(counter)
        counter = counter + 1
        arr.append(i)
    print(arr[3])
    # temp = soup_handler.find(id="pitching_standard.2019")
    # for i in temp:
    #     print(i.text)



if __name__ == '__main__':
    scrape_data_website()