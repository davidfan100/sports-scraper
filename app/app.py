from flask import Flask, render_template, request
import sqlite3
import json
'''
- create a flask app 
- create panels that display stats of players EXCEPT with either height or weight emphasized
- for now just do two screens with display data for weight or height (height and weight could just be options)
- one bubble chart displays the chosen stat, other one line chart displays either height or weight
- my new feature is that I can compare using weight and height, which isn't common in other webistes
- grab data from sql datatable
- using d3 js
'''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/', methods=['POST'])
def home_post():
    data_dict = request.form.to_dict()

    # list stats that need don't need to be sorted
    non_sorted_stats = ['ERA', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9']

    is_desc = "DESC"
    if data_dict['Stat'] in non_sorted_stats:
        is_dec = ""
    
    sql_query = '''
    select name, {}, {} from PitchingStats where Year={} and IP >= 162 order by {} {} LIMIT 10
    '''.format(data_dict['Stat'], data_dict['Measure'], data_dict['Year'], data_dict['Stat'], is_desc)

    conn = sqlite3.connect('../data/baseballtable.db')
    cur = conn.cursor()
    
    cur.execute(sql_query)
    format_dict = {}

    for row in cur.fetchall():
        format_dict[row[0]] = {}
        format_dict[row[0]]['Stat'] = row[1]
        format_dict[row[0]]['Measure'] = row[2]

    return json.dumps(format_dict)
if __name__ == '__main__':
    app.run(debug=True)