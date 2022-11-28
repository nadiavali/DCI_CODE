# Popular convection
# Singular form of class name to represent a table
# table will be mostly plural
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="flask_intro",
)

cur = connection.cursor()


class Reminder:
    # Serial data types  -- numbers that are increases 1, 2, 3, etc.
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def save(self):
        '''
        Stores the title and description in the table
        '''
        cur.execute(f"""INSERT INTO reminders (title, description) 
            VALUES('{self.title}', '{self.description}') RETURNING id, title, description""")
        #persist the changes
        connection.commit()

        # Return the instance
        values = cur.fetchone()
        print(values)

    