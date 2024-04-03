import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
    )

# prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
