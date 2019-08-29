'''
- First import the sqlite and beautiful soup (web scrapping) libraries
- Create a function to collect the information from baseball reference using beautiful soup
- Then create an sql database and create tables based on player's name alphabetically
- add height/weight to the database to be able to filter and organize on the webapp
'''

import sqlite3
import requests
import logging
import datetime
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


    '''
    Start from most recent year and then go backwards to see if there exists a
    value for them
    '''

    page_info = soup_handler.find(id='meta')
    player_height = page_info.find('span', {'itemprop': 'height'}).text
    temp_height =  player_height.split('-')
    player_height = int(temp_height[0]) * 12 + int(temp_height[1])
    player_weight = page_info.find('span', {'itemprop': 'weight'}).text[:-2]
    player_name = page_info.find('h1', {'itemprop': 'name'}).text

    for temp_i in page_info.find_all('a'):
        if 'play-index' in temp_i.get('href'):
            # determining player's debut year
            curr_year = int(temp_i.text.split()[-1])
            break

    player_years = {}
    player_years[str(curr_year)] = []
    most_recent_year = datetime.datetime.now().year

    while curr_year <= int(most_recent_year):
        if str(curr_year) not in player_years.keys():
            player_years[str(curr_year)] = []

        curr_year_stats = soup_handler.find(id="pitching_standard.{}".format(str(curr_year)))
        
        if curr_year_stats != None:
            player_years[str(curr_year)].append([])
            player_years[str(curr_year)][-1].append(player_name)
            player_years[str(curr_year)][-1].append(curr_year)

            for stat_val in curr_year_stats.find_all('td'):
                player_years[str(curr_year)][-1].append(stat_val.text)

            player_years[str(curr_year)][-1].append(player_height)
            player_years[str(curr_year)][-1].append(player_weight)
        curr_year += 1

    print(player_years)
        
    # determine a way to go through each row to extract the data


if __name__ == '__main__':
    scrape_data_website()