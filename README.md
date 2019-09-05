# sports-scraper
A web scrapper that will obtain mlb players baseball statistics and store it into
an sql table. The data will contain the typical stats as from the website except with height
and weight added. The data will obtain data from 2015 to 2019 and contains only current playaers 
(meaning some players in 2017 may be left off because they aren't playing currently)

The web application will have users choose specific statistics for players based on a year and will then
have a bubble graph displaying the chosen stat's top 10 players and a line graph that displays
those players' height or weight. 
e.g. User chooses OPS, then the bubble graph will show the top 10 players

Utilized: Beautiful Soup, sqlite3, Flask, Bootstrap, d3.js

**Data is from baseball reference**
