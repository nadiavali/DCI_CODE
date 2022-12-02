# export FLASK_APP=flaskblog.py
#flask run
#export FLASK_DEBUG=1 #to can make as much change'as we need withot crl+c

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>This is a Header!</h1>"  # heading text in html 

@app.route("/about")
def about():
    return "<h1>About!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
