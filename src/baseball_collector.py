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
    start_url = 'https://www.baseball-reference.com/players/'
    base_url = 'https://www.baseball-reference.com'
    curr_letter = 'a'
    urls_list = []

    while curr_letter <= 'z':
        curr_url = start_url + curr_letter
        response = requests.get(curr_url)
    
        soup_handler = BeautifulSoup(response.text, "html.parser")
        temp = soup_handler.find_all('b') # bold means the player are active

        urls = []
        for i in temp:
            if i.a == None:
                continue
        
            urls.append(base_url + i.a.get('href'))

        if urls != []:
            urls_list.append(urls)
        
        curr_letter = chr(ord(curr_letter) + 1)
        
    player_years = {}
    most_recent_year = datetime.datetime.now().year
    
    for url_arr in urls_list:
        print(url_arr[0])
        for url in url_arr:
            player_url = url
            response = requests.get(player_url)
            soup_handler = BeautifulSoup(response.text, 'html.parser')

            if (soup_handler.find(id="pitching_standard.{}".format(str(most_recent_year))) == None
                and soup_handler.find(id="batting_standard.{}".format(str(most_recent_year))) == None):
                continue 
        
            page_info = soup_handler.find(id='meta')

            player_height = page_info.find('span', {'itemprop': 'height'}).text
            temp_height =  player_height.split('-')
            player_height = int(temp_height[0]) * 12 + int(temp_height[1])

            player_weight = int(page_info.find('span', {'itemprop': 'weight'}).text[:-2])

            player_name = page_info.find('h1', {'itemprop': 'name'}).text

            for temp_i in page_info.find_all('a'):
                if 'play-index' in temp_i.get('href'):
                    # determining player's debut year
                    curr_year = int(temp_i.text.split()[-1])
                    break
        
            while curr_year <= int(most_recent_year):
                if str(curr_year) not in player_years.keys():
                    player_years[str(curr_year)] = []

                curr_year_stats = soup_handler.find(id="pitching_standard.{}".format(str(curr_year)))
        
                if curr_year_stats == None:
                    curr_year_stats = soup_handler.find(id='batting_standard.{}'.format(str(curr_year)))
                
                if curr_year_stats != None:
                    player_years[str(curr_year)].append([])

                    if "'" in player_name:
                        player_years[str(curr_year)][-1].append("'{}'".format(player_name[0:player_name.index("'")] + 
                            player_name[player_name.index("'") + 1:]))
                        # print(player_name)
                    else:
                        player_years[str(curr_year)][-1].append("'{}'".format(player_name))
                    
                    player_years[str(curr_year)][-1].append(str(curr_year))

                    for stat_val in curr_year_stats.find_all('td'):
                        if ('.' in stat_val.text or stat_val.text.isdigit()):
                            player_years[str(curr_year)][-1].append(stat_val.text)
                        else:
                            player_years[str(curr_year)][-1].append("'{}'".format(str(stat_val.text)))


                    player_years[str(curr_year)][-1].append(str(player_height))
                    player_years[str(curr_year)][-1].append(str(player_weight))
                
                curr_year += 1

    return player_years

def create_tables(batting_stats, pitching_stats):
    conn = sqlite3.connect('../data/baseballtable.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE PitchingStats
        ({})
    '''.format(','.join(pitching_stats)))

    cur.execute('''
        CREATE TABLE BattingStats
        ({})
    '''.format(','.join(batting_stats)))

    conn.commit()
    conn.close()


def transfer_to_sql_table(data):
    conn = sqlite3.connect('../data/baseballtable.db')
    cur = conn.cursor()

    print("Inserting into SQL Table...")
    # temp_arr = ["'Fernando Abad'", '2010', '24', "'HOU'", "'NL'", '0', '1', '0.0', '2.84', '22', '0', '6', '0', '0', '0', '19.0', '14', '6', '6', '3', '5', '0', '12', '0', '0', '0', '76', '142', '4.66', '1.0', '6.6', '1.4', '2.4', '5.7', '2.4', "''", '73', '220']

    # a = ','.join(temp_arr)
    # print(a)
    # cur.execute('''
    #     INSERT INTO PitchingStats VALUES ({})
    # '''.format(a))
    for year in data.keys():
        print('Current year: {}'.format(year))
        for player_stats in data[year]:
            print(player_stats)
            if len(player_stats) == 38:
                # print(player_stats)
                print('Insert to pitching')
                cur.execute('''
                    INSERT INTO PitchingStats VALUES ({})
                '''.format(','.join(player_stats)))
            else:
                print('Insert to batting')
                cur.execute('''
                    INSERT INTO BattingStats VALUES ({})
                '''.format(','.join(player_stats)))
    

    conn.commit()
    conn.close()

    
if __name__ == '__main__':
    player_years = scrape_data_website()

    batting_stats = ['Name text', 'Year int', 'Age int', 'Team text', 'League text', 'GamesPlayed int', 'PlateAppearances int', 'AtBats int', 'Runs int', 'Hits int', 'Doubles int', 'Triples int',
        'HR int', 'RBI int', 'SB int', 'CS int', 'BB int', 'SO int', 'BA real', 'OBP real', 'SLG real', 'OPS real', 'OPSPlus real', 'TB int', 'GBP int', 'HBP int', 'SH int', 'SF int', 'IBB int', 'Pos text', 'Awards text',
        'Height int', 'Weight int']

    pitching_stats = ['Name text', 'Year int', 'Age int', 'Team text', 'League text', 'W int', 'L int', 'WinLossPercentage real', 'ERA real', 'G int', 'GS int', 'GF int', 'CG int',
        'SHO int', 'SV int', 'IP real', 'H int', 'R int', 'ER real', 'HR int', 'BB int', 'IBB int', 'SO int', 'HBP int', 'BK int', 'WP int', 'BF int', 'ERAPLUS int', 'FIP real', 'WHIP real',
        'H9 real', 'HR9 real', 'BB9 real', 'SO9 real', 'StrikeoutsPerWalk real', 'Awards text', 'Height int', 'Weight int']

    # create_tables(batting_stats, pitching_stats)

    # Run to generate the sql table
    transfer_to_sql_table(player_years)