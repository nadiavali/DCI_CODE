# export FLASK_APP=flaskblog.py
#flask run
#export FLASK_DEBUG=1 #to can make as much change'as we need without crl+c

from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {   "author": "Nadia",
        "title": "Hello World",
        "content": "This is my first blog post.",
        "date_posted":'April 20, 2020'
    },
    {   "author": "Corey", 
        "title": "Hello Nadia",
        "content": "This is my second blog post.",
        "date_posted":'April 22, 2020'
    }

]
@app.route("/")
#@app.route("/home") # two routs do the same thing
def home():
    return render_template('home.html', posts=posts)  # heading text in html 
@app.route("/about") # each page and method you create you need to make a route first for that
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__': # this helps us to run it without exporting and running flask # Python3 flaskblog.py
    app.run(debug=True)
