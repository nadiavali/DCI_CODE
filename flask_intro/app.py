from flask import Flask, jsonify, request
#connect data base
import psycopg2



#instantiating a class(flask)
app = Flask(__name__)

#home  or Root or route
#methods that represent URLS or links
REMINDERS = ['HEY']


@app.route('/')
def index():
    return jsonify({'name': 'Nadia'})
    #return jsonify('string')
    #return jsonify('anything but turns a tuple into a list but popular to send back a dict')

#we want to store 'reminders'
#how do we save the reminders?


@app.route('/add-reminder', methods=['POST'])  #add-reminder is url
def add_reminder():
    print(request.json)
    REMINDERS.append(request.json)
    # jsonify takes a dict and return some special data format #we are designing an API
    return jsonify({'reminders':REMINDERS})
    
#core HTTP verbs a developers must know

#get

# # Exercise, add the reminders (dictionaries) to the REMINDERS constant

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug =True, port=5050)