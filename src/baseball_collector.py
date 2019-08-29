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


    '''
    Start from most recent year and then go backwards to see if there exists a
    value for them
    '''

    page_info = soup_handler.find(id='meta')
    player_height = page_info.find('span', {'itemprop': 'height'}).text
    temp_height =  player_height.split('-')
    player_height = int(temp_height[0]) * 12 + int(temp_height[1])
    player_weight = page_info.find('span', {'itemprop': 'weight'}).text[:-2]

    for temp_i in page_info.find_all('a'):
        if 'play-index' in temp_i.get('href'):
            player_debut = temp_i.text.split()[-1]
            break

    print(player_height)
    print(player_weight)
    print(player_debut)
    # player_years = {}
    # player_years['2019'] = []
    # curr_year = 2019

    # while True:
    #     if str(curr_year) not in player_years.keys():
    #         player_years[str(curr_year)] = []
        
    #     curr_year_stats = soup_handler.find(id="pitching_standard.{}".format(str(curr_year)))
        
    #     if curr_year_stats == None:
    #         break
        
    #     player_years[str(curr_year)].append([])
    #     player_years[str(curr_year)][-1].append(curr_year)

    #     for stat_val in curr_year_stats.find_all('td'):
    #         player_years[str(curr_year)][-1].append(stat_val.text)

    #     curr_year -= 1

    # print(player_years)
        
    # determine a way to go through each row to extract the data


if __name__ == '__main__':
    scrape_data_website()