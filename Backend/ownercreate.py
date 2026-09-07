import sqlite3

connection = sqlite3.connect("Backend/AquaparkBd")
cursor = connection.cursor()

cursor.execute("UPDATE Users SET role = 'Owner' WHERE name = 'Низами'")
connection.commit()
connection.close()