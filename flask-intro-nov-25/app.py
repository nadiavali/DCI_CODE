# TODO: Goal -> https://github.com/Python-E03/live-coding-reminder-application-teamrando/issues/45 

from flask import Flask, jsonify, request
import psycopg2
#ORM -> object Relational Mapper
# 'Class' represents the Table (relation)
# an instance of that class (object), refers to the single record in the table

# Designers have to make some choices
#Algorithm
# - Create instances of the class
# - Then call the save() method of that instance

# Nadia = Person(1, 'Nadia', 'Berlin')
# Nadia.save() #--> psql --> INSERT INTO
# Nadia.delete() #--> psql --> DELETE FROM
# Nadia.update() #--> psql --> UPDATE people SET  


# static methods --------------------------------
# Person.find(23) #--> psql --> SELECT * FROM people WHERE id = 23;
# class Person:
#     def __init__(self, name, location): # class represents the table
#         self.name = name
#         self.location = location

# Nadia = Person(1, 'Nadia', 'Berlin') # instance of the class -> record in the table



app = Flask(__name__)

@app.route("/")
def index():
    # Fetch all the reminders from the database
    cur.execute("SELECT id, title, description FROM reminders")
    reminder_data = cur.fetchall()
    reminder_data = [
        {"id": item[0], "title": item[1], "description": item[2]}
        for item in reminder_data
    ]
    return jsonify({"reminders": reminder_data})

@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    try:
        title = request.json["title"]
    except KeyError:
        title = None

    # handle the exception (error handling)
    try:
        description = request.json["description"]
    except KeyError:
        description = None
    cur.execute(
        f"INSERT INTO reminders (title, description) VALUES('{title}', '{description}') RETURNING id, title, description;"
    )
    connection.commit()
    values = cur.fetchone()
    print(values)
    # change the return value from empty list to have REMINDERS instead
    return jsonify({})


@app.route("/reminders/<int:id>")
def reminder(id):
    cur.execute(f"SELECT title, description FROM reminders WHERE id = {id};")
    reminder_data = cur.fetchone()
    if not reminder_data:
        return jsonify({"message": "Reminder not found"}), 404
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data[0],
            "description": reminder_data[1],
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "Sorry something bad happened"}), 500


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    cur.execute(f"DELETE FROM reminders WHERE id={id};")
    # commit the changes
    connection.commit()
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    cur.execute(
        f"""
        UPDATE reminders
        SET title='{request.json.get('title')}', 
        description='{request.json.get('description')}'
        WHERE id={id} RETURNING id, title, description
    """
    )
    breakpoint()
    values = cur.fetchone()
    connection.commit()
    try:
        return jsonify({"id": values[0], "title": values[1], "description": values[2]})
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
