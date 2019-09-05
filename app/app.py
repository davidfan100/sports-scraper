from flask import Flask, render_template

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
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run(debug=True)