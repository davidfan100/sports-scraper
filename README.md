# sports-scraper-application

## Goal
To create an application that will show any correlations between a player's body measurement and performance
statistic for choosing better players in fantasy baseball drafting

## Description
A web scrapper that will obtain mlb players baseball statistics and store it into
an sql table. The data will contain the typical stats as from the website except with height
and weight added. The data will obtain data from 2015 to 2019 and contains only current playaers 
(meaning some players in 2017 may be left off because they aren't playing currently)

The web application will have users choose specific statistics for players based on a year and will then
have a bubble graph displaying the chosen stat's top 10 players and a line graph that displays
those players' height or weight. 
e.g. User chooses OPS, then the bubble graph will show the top 10 players

## Dependencies
* Beautiful Soup
* sqlite3
* Flask
* Bootstrap
* d3.js

## How to run this application
1. Clone this repo
2. Install the necessary dependencies
3. CD into the app directory and run the command **python3 app.py**
4. Access the application on 127.0.0.1:5000 in your local browser

TODO: Implement the Bubble Chart
**Data is from baseball reference**
